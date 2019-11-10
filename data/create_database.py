import sqlite3, os

FILENAME = 'web.db'

if FILENAME in os.listdir():
	os.remove(FILENAME)

create_w_all = """
	CREATE TABLE w_all (
		branch varchar(5),
		branch_name varchar(50),
		status varchar(20),
		sales int,
		purchase_value float,
		revenue float,
		tgt_delivery int,
		act_delivered int,
		employee int);
	"""

create_w_sales_history = """
	CREATE TABLE w_sales_history (
		yearmonth varchar(4),
		sales int,
		purchase_cat1 float,
		purchase_cat2 float,
		purchase_cat3 float,
		purchase_cat4 float);
	"""

create_w_jual = """
	CREATE TABLE w_jual (
		tipe varchar(20),
		urut tinyint,
		nama varchar(50),
		nilai int);
	"""

create_w_jual_hari = """
	CREATE TABLE w_jual_hari (
		tgl date,
		awb int,
		rp float);
	"""

create_w_pod = """
	CREATE TABLE w_pod (
		tipe varchar(20),
		urut tinyint,
		nama varchar(50),
		nilai int);
	"""

create_w_kurir = """
	CREATE TABLE w_kurir (
		cab varchar(5),
		nama_cab varchar(50),
		kurir varchar(10),
		nama_kurir varchar(50),
		sdep varchar(20),
		pod_non_cod int,
		pod_cod int,
		pod_total int);
	"""

insert_w_all = """
	INSERT INTO w_all values
		('001', 'BRANCH JAKARTA', 'ACTIVE', 254809, 6205364000, 806697000, 236108, 231976, 35),
		('002', 'BRANCH BANDUNG', 'ACTIVE', 253183, 4621349000, 600775000, 261095, 258354, 30),
		('003', 'BRANCH SURABAYA', 'ACTIVE', 157182, 3361494000, 336149000, 151018, 148118, 28),
		('004', 'BRANCH SEMARANG', 'ACTIVE', 93657, 1992740000, 139492000, 90819, 90383, 28),
		('005', 'BRANCH DENPASAR', 'ACTIVE', 25107, 585495000, 81969000, 23864, 23229, 28);
	"""

insert_w_sales_history = """
	INSERT INTO w_sales_history values
		('1701', 254392, 2100029000, 1776948000, 915398000, 592316000),
		('1702', 263168, 1988071000, 1733188000, 815620000, 560738000),
		('1703', 270323, 2114330000, 2228617000, 685729000, 685727000),
		('1704', 279079, 1982617000, 2139141000, 626090000, 469568000),
		('1705', 321390, 2125142000, 2184173000, 1003539000, 590318000),
		('1706', 302726, 2214031000, 2337032000, 799510000, 799513000),
		('1707', 337303, 2407754000, 2273990000, 1203877000, 802585000),
		('1708', 342423, 1950712000, 2423611000, 827574000, 709350000),
		('1709', 365119, 2152071000, 2985132000, 971903000, 833059000),
		('1710', 401598, 2408985000, 3462916000, 903369000, 752811000),
		('1711', 383384, 2331696000, 3098035000, 851773000, 609055000),
		('1712', 406805, 2751765000, 3075503000, 1456816000, 809342000),
		('1801', 411988, 3178985000, 2852935000, 1059661000, 1059662000),
		('1802', 424515, 2446725000, 3157064000, 1420678000, 868194000),
		('1803', 445540, 3962892000, 3759667000, 1524190000, 914513000),
		('1804', 471767, 2701990000, 3546363000, 1182122000, 1013242000),
		('1805', 457187, 3900234000, 4216471000, 1475764000, 948707000),
		('1806', 465102, 2804540000, 3768600000, 1139345000, 1051700000),
		('1807', 509146, 2850507000, 3990710000, 1615287000, 1045185000),
		('1808', 538680, 3479908000, 3901714000, 1898131000, 1265422000),
		('1809', 568867, 3306256000, 5069591000, 1322503000, 1322500000),
		('1810', 551916, 4517669000, 4291787000, 1468243000, 1016474000),
		('1811', 566977, 4065072000, 5245252000, 2229234000, 1573576000),
		('1812', 602090, 3999945000, 4342797000, 1942830000, 1142840000),
		('1901', 621492, 4872934000, 5549730000, 1895030000, 1218233000),
		('1902', 645792, 5069768000, 4802938000, 2134639000, 1334150000),
		('1903', 662189, 4446356000, 6224899000, 2519601000, 1630332000),
		('1904', 670803, 5076300000, 5972118000, 2388847000, 1493030000),
		('1905', 663933, 4780827000, 5179229000, 1992011000, 1328007000),
		('1906', 696885, 5059222000, 3920897000, 2150169000, 1517766000),
		('1907', 722679, 6248642000, 5590888000, 2959882000, 1644380000),
		('1908', 737364, 6105975000, 5037430000, 2289741000, 1831793000),
		('1909', 748533, 5153250000, 5582688000, 2147187000, 1431459000),
		('1910', 739122, 4303903000, 6108765000, 1943698000, 1527194000),
		('1911', 771063, 5227980000, 6495369000, 2534778000, 1584235000),
		('1912', 783938, 6538913000, 5868254000, 2179636000, 2179639000);
	"""

insert_w_jual = """
	INSERT INTO w_jual values
		('byr', 1, 'TUNAI', 94371),
		('byr', 2, 'KREDIT', 164332),
		('byr', 3, 'COD', 4823),
		('cod', 1, 'COD ONGKIR SAJA          ', 5282),
		('cod', 2, 'COD ONGKIR + BARANG', 2831),
		('cod', 3, 'COD BARANG SAJA         ', 781),
		('cab', 1, 'BRANCH JAKARTA', 6205364000),
		('cab', 2, 'BRANCH BANDUNG', 4621349000),
		('cab', 3, 'BRANCH SURABAYA', 3361494000),
		('cab', 4, 'BRANCH SEMARANG', 1992740000),
		('cab', 5, 'BRANCH DENPASAR', 585495000),
		('kons', 1, 'KONSUMEN ABC', 82301000),
		('kons', 2, 'KONSUMEN DEF', 67125000),
		('kons', 3, 'KONSUMEN GHI', 424323000),
		('kons', 4, 'KONSUMEN JKL', 230394000),
		('kons', 5, 'KONSUMEN MNO', 182329000);
	"""

insert_w_jual_hari = """
	INSERT INTO w_jual_hari values
		('2019-12-02', 37909, 751137000),
		('2019-12-03', 28537, 565029000),
		('2019-12-04', 63290, 1150178000),
		('2019-12-05', 46462, 386706000),
		('2019-12-06', 87112, 939281000),
		('2019-12-09', 53970, 1016046000),
		('2019-12-10', 56008, 1383231000),
		('2019-12-11', 67829, 1448621000),
		('2019-12-12', 49373, 1177004000),
		('2019-12-13', 26960, 581796000),
		('2019-12-16', 45879, 1141795000),
		('2019-12-17', 20926, 409101000),
		('2019-12-18', 41039, 504670000),
		('2019-12-19', 60456, 1319519000),
		('2019-12-20', 42715, 601915000),
		('2019-12-23', 62738, 1388261000),
		('2019-12-24', 42364, 741077000),
		('2019-12-25', 22465, 439281000),
		('2019-12-26', 8883, 186108000),
		('2019-12-27', 54614, 509700000),
		('2019-12-30', 7718, 169341000),
		('2019-12-31', 31768, 556646000);
	"""

insert_w_pod = """
	INSERT INTO w_pod values
		('all', 1, 'DONE (Z) BELUM JTP', 91239),
		('all', 2, 'DONE (Z) LEWAT JTP', 82371),
		('all', 3, 'NOT DONE BELUM JTP', 23129),
		('all', 4, 'NOT DONE LEWAT JTP', 14921),
		('all', 5, 'RETUR (X)', 821),
		('notdonelewatjtp', 1, '1 hari', 23914),
		('notdonelewatjtp', 2, '2 hari', 12742),
		('notdonelewatjtp', 3, '3 hari', 7993),
		('notdonelewatjtp', 4, '4 hari', 3792),
		('notdonelewatjtp', 5, '5 hari', 3583),
		('notdonelewatjtp', 6, '6 hari', 1492),
		('notdonelewatjtp', 7, '7 hari', 821),
		('notdonelewatjtp', 8, '8-14 hari', 491),
		('notdonelewatjtp', 9, '15-30 hari', 102),
		('notdonelewatjtp', 10, 'diatas 30 hari', 46),
		('cab', 1, 'BRANCH JAKARTA', 3881),
		('cab', 2, 'BRANCH BANDUNG', 1291),
		('cab', 3, 'BRANCH SURABAYA', 523),
		('cab', 4, 'BRANCH SEMARANG', 299),
		('cab', 5, 'BRANCH DENPASAR', 331);
	"""

insert_w_kurir = """
	INSERT INTO w_kurir values
		('001', 'BRANCH JAKARTA', '1089412', 'KURIR 1', 'KURIR', 8221, 471, 8692),
		('001', 'BRANCH JAKARTA', '1089412', 'KURIR 2', 'KURIR', 8221, 471, 8692),
		('001', 'BRANCH JAKARTA', '1089412', 'KURIR 3', 'KURIR', 8221, 471, 8692),
		('001', 'BRANCH JAKARTA', '1089412', 'KURIR 4', 'KURIR', 8221, 471, 8692);
	"""


con = sqlite3.connect(FILENAME)
cur = con.cursor()

cur.execute(create_w_all)
cur.execute(create_w_sales_history)
cur.execute(create_w_jual)
cur.execute(create_w_jual_hari)
cur.execute(create_w_pod)
cur.execute(create_w_kurir)
cur.execute(insert_w_all)
con.commit()
cur.execute(insert_w_sales_history)
con.commit()
cur.execute(insert_w_jual)
con.commit()
cur.execute(insert_w_jual_hari)
con.commit()
cur.execute(insert_w_pod)
con.commit()
cur.execute(insert_w_kurir)
con.commit()