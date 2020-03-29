import sqlite3, os, hashlib, datetime

FILENAME = 'web.db'

if FILENAME in os.listdir():
    os.remove(FILENAME)

sql_script = """
	CREATE TABLE w_all (
		branch VARCHAR(5),
		branch_name VARCHAR(50),
		status VARCHAR(20),
		sales INT,
		purchase_value FLOAT,
		revenue FLOAT,
		tgt_delivery INT,
		act_delivered INT,
		employee INT);

	CREATE TABLE w_sales_history (
		yearmonth VARCHAR(4),
		sales INT,
		purchase_cat1 FLOAT,
		purchase_cat2 FLOAT,
		purchase_cat3 FLOAT,
		purchase_cat4 FLOAT);

	CREATE TABLE w_sales (
		type VARCHAR(20),
		sort TINYINT,
		name VARCHAR(50),
		value INT);

	CREATE TABLE w_sales_days (
		date DATE,
		sales INT,
		purchase_value FLOAT);

	CREATE TABLE w_delivery (
		type VARCHAR(20),
		sort TINYINT,
		name VARCHAR(50),
		value INT);

	CREATE TABLE w_courier (
		branch VARCHAR(5),
		branch_name VARCHAR(50),
		courier VARCHAR(10),
		courier_name VARCHAR(50),
		division VARCHAR(20),
		delivery_regular INT,
		delivery_cod INT,
		delivery_total INT);

	CREATE TABLE w_user (
		username VARCHAR(20),
		password VARCHAR(255),
		datetime_register DATETIME,
		datetime_last_login DATETIME,
		count_login INT);

	CREATE TABLE w_branch (
		branch VARCHAR(5),
		branch_name VARCHAR(50),
		address VARCHAR(255),
		latitude FLOAT,
		longitude FLOAT);

    CREATE TABLE w_galery (
		type VARCHAR(10),
        title VARCHAR(50),
        description VARCHAR(255),
        duration INT,
        filename VARCHAR(50),
        thumbnail VARCHAR(50));

	CREATE TABLE w_tracking (
		awb VARCHAR(20),
        origin VARCHAR(50),
        destination VARCHAR(255),
        service INT,
        date VARCHAR(50),
		shipper VARCHAR(50),
		consignee VARCHAR(50));

	CREATE TABLE w_tracking_detail (
		awb VARCHAR(20),
        date VARCHAR(50),
		tlc VARCHAR(5),
		note VARCHAR(50));

	CREATE TABLE w_city (
		tlc VARCHAR(5),
        name VARCHAR(50));

	CREATE TABLE w_tariff (
		origin VARCHAR(5),
        destination VARCHAR(5),
        service VARCHAR(20),
        price INT,
        etd INT);

	INSERT INTO w_all values
		('001', 'BRANCH JAKARTA', 'ACTIVE', 254809, 6205364000, 806697000, 236108, 231976, 35),
		('002', 'BRANCH BANDUNG', 'ACTIVE', 253183, 4621349000, 600775000, 261095, 258354, 30),
		('003', 'BRANCH SURABAYA', 'ACTIVE', 157182, 3361494000, 336149000, 151018, 148118, 28),
		('004', 'BRANCH SEMARANG', 'ACTIVE', 93657, 1992740000, 139492000, 90819, 90383, 28),
		('005', 'BRANCH DENPASAR', 'ACTIVE', 25107, 585495000, 81969000, 23864, 23229, 28);

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

	INSERT INTO w_sales values
		('payment', 1, 'CASH', 94371),
		('payment', 2, 'CREDIT', 164332),
		('payment', 3, 'CASH ON DELIVERY', 4823),
		('source', 1, 'ORGANIC', 5282),
		('source', 2, 'PAID', 2831),
		('source', 3, 'REFERRAL', 781),
		('branch', 1, 'BRANCH JAKARTA', 6205364000),
		('branch', 2, 'BRANCH BANDUNG', 4621349000),
		('branch', 3, 'BRANCH SURABAYA', 3361494000),
		('branch', 4, 'BRANCH SEMARANG', 1992740000),
		('branch', 5, 'BRANCH DENPASAR', 585495000),
		('customer', 1, 'CUSTOMER ABC', 82301000),
		('customer', 2, 'CUSTOMER DEF', 67125000),
		('customer', 3, 'CUSTOMER GHI', 424323000),
		('customer', 4, 'CUSTOMER JKL', 230394000),
		('customer', 5, 'CUSTOMER MNO', 182329000);

	INSERT INTO w_sales_days values
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

	INSERT INTO w_delivery values
		('all', 1, 'SENT ON TIME', 91239),
		('all', 2, 'SENT LATE', 82371),
		('all', 3, 'ON PROGRESS NOT LATE', 23129),
		('all', 4, 'ON PROGRESS LATE', 14921),
		('all', 5, 'RETURN', 821),
		('deliverylate', 1, '1 day', 23914),
		('deliverylate', 2, '2 days', 12742),
		('deliverylate', 3, '3 days', 7993),
		('deliverylate', 4, '4 days', 3792),
		('deliverylate', 5, '5 days', 3583),
		('deliverylate', 6, '6 days', 1492),
		('deliverylate', 7, '7 days', 821),
		('deliverylate', 8, '8-14 days', 491),
		('deliverylate', 9, '15-30 days', 102),
		('deliverylate', 10, 'more than 30 days', 46),
		('branch', 1, 'BRANCH JAKARTA', 3881),
		('branch', 2, 'BRANCH BANDUNG', 1291),
		('branch', 3, 'BRANCH SURABAYA', 523),
		('branch', 4, 'BRANCH SEMARANG', 299),
		('branch', 5, 'BRANCH DENPASAR', 331);

	INSERT INTO w_courier values
		('001', 'BRANCH JAKARTA', '1089412', 'KURIR 1', 'KURIR', 8221, 471, 8692),
		('002', 'BRANCH BANDUNG', '2947391', 'KURIR 2', 'KURIR', 9309, 642, 9951),
		('003', 'BRANCH SURABAYA', '3010021', 'KURIR 3', 'KURIR', 7351, 183, 7534),
		('004', 'BRANCH SEMARANG', '3100375', 'KURIR 4', 'KURIR', 1738, 481, 2219),
		('005', 'BRANCH DENPASAR', '3683619', 'KURIR 5', 'KURIR', 882, 74, 956);

	INSERT INTO w_user values
		('admin', '{}', '{}', null, 0),
		('user', '{}', '{}', null, 0);

	INSERT INTO w_branch values
		('001', 'BRANCH JAKARTA', 'Jalan A.M Sangaji No. 22-24, Petojo Utara, Gambir, Kota Jakarta Pusat', -6.167521, 106.813580),
		('002', 'BRANCH BANDUNG', 'Jl. Diponegoro No.22, Citarum, Bandung Wetan, Kota Bandung, Jawa Barat', -6.902247, 107.618826),
		('003', 'BRANCH SURABAYA', 'Jl. Kusuma Bangsa No.21, Ketabang, Genteng, Kota Surabaya, Jawa Timur', -7.256910, 112.750198),
		('004', 'BRANCH SEMARANG', 'Jl. Pemuda No.149, RT.5/RW.3, Sekayu, Semarang Tengah, Kota Semarang, Jawa Tengah', -6.980656, 110.412398),
		('005', 'BRANCH DENPASAR', 'Jl. Gunung Rinjani No.1, Tegal Harum, Denpasar Barat, Kota Denpasar, Bali', -8.663904, 115.199484);
    
    INSERT INTO w_galery values
        ('video', 'Cleaning Hand', 'Cleaning hand with hand sanitizer source: coverr.co', 1, 'cleaning-hand.mp4', 'cleaning-hand.jpg'),
        ('video', 'Flying Birds', 'Flying birds animation source: coverr.co', 1, 'Flying-Birds.mp4', 'Flying-Birds.jpg'),
        ('video', 'People Walking', 'People walking down the NYC source: coverr.co', 1, 'Going-Places.mp4', 'Going-Places.jpg'),
        ('video', 'Laptop Typing', 'Female hand typing laptop source: coverr.co', 1, 'laptop-typing.mp4', 'laptop-typing.jpg'),
		('image', 'Cargo Ship', 'Cargo ship from above source: pexels.com', 0, 'cargo-ship.jpg', 'cargo-ship.jpg'),
		('image', 'Warehouse', 'Warehouse source: pexels.com', 0, 'warehouse.jpg', 'warehouse.jpg'),
		('image', 'Forklift', 'Forklift at our warehouse source: pexels.com', 0, 'forklift.jpg', 'forklift.jpg'),
		('image', 'Container Truck', 'Container Truck across country source: pexels.com', 0, 'container.jpg', 'container.jpg');

	INSERT INTO w_tracking values
        ('CGK191212341234', 'Jakarta', 'Demak', 'REG', '2019-12-04 09:32:17', 'Budi', 'Ani');
	
	INSERT INTO w_tracking_detail values
        ('CGK191212341234', '2019-12-04 09:32:17', 'CGK', 'Received by Counter at Jakarta'),
		('CGK191212341234', '2019-12-04 13:11:56', 'CGK', 'Sorted by Sorting Center at Jakarta'),
		('CGK191212341234', '2019-12-04 17:49:05', 'CGK', 'Create Manifest at Jakarta'),
		('CGK191212341234', '2019-12-04 21:25:39', 'SRG', 'Departed from Jakarta to Semarang'),
		('CGK191212341234', '2019-12-05 10:38:13', 'SRG', 'Transit at Semarang'),
		('CGK191212341234', '2019-12-05 11:51:48', 'SRG', 'Departed from Semarang to Demak'),
		('CGK191212341234', '2019-12-05 13:43:24', 'DMK', 'Received by Inbound Demak'),
		('CGK191212341234', '2019-12-05 15:32:56', 'DMK', 'Deliver by courier Tono'),
		('CGK191212341234', '2019-12-05 16:07:12', 'DMK', 'Delivered to Ani');

    INSERT INTO w_city values
        ('CGK', 'Jakarta'),
        ('SRG', 'Semarang');

    INSERT INTO w_tariff values
        ('CGK', 'SRG', 'REG', 15000, 3),
        ('CGK', 'SRG', 'ONEDAY', 20000, 1),
        ('CGK', 'SRG', 'FLASH', 25000, 0);
	""".format(hashlib.sha1('admin'.encode('utf-8')).hexdigest(), datetime.datetime.now(), hashlib.sha1('user'.encode('utf-8')).hexdigest(), datetime.datetime.now())

con = sqlite3.connect(FILENAME)
cur = con.cursor()

cur.executescript(sql_script)