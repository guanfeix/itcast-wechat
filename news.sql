LOCK TABLES `wechat_academyinfo` WRITE;
/*!40000 ALTER TABLE `wechat_academyinfo` DISABLE KEYS */;
INSERT INTO `wechat_academyinfo` VALUES (1,'C/C++','萧峰','C语言是在70年代初问世的。一九七八年由美国电话电报公司(AT&T)贝尔实验室正式发表了C语言。同时由B.W.Kernighan和D.M.Ritchit合著了著名的“THE C PROGRAMMING LANGUAGE”一书。通常简称为《K&R》，也有人称之为《K&R》标准。但是，在《K&R》中并没有定义一个完整的标准C语言，后来由美国国家标准学会在此基础上制定了一个C 语言标准，于一九八三年发表。通常称之为ANSI C。','cc','upload/cplusplus_xe3xJ8T.jpg'),(2,'PHP','小倩','PHP（外文名:PHP: Hypertext Preprocessor，中文名：“超文本预处理器”）是一种通用开源脚本语言。语法吸收了C语言、Java和Perl的特点，利于学习，使用广泛，主要适用于Web开发领域。PHP 独特的语法混合了C、Java、Perl以及PHP自创的语法。它可以比CGI或者Perl更快速地执行动态网页。用PHP做出的动态页面与其他的编程语言相比，PHP是将程序嵌入到HTML（标准通用标记语言下的一个应用）文档中去执行，执行效率比完全生成HTML标记的CGI要高许多；PHP还可以执行编译后代码，编译可以达到加密和优化代码运行，使代码运行更快。','php','upload/php_3pVEzm3.jpg'),(3,'Java','浪子回头','Java是一种可以撰写跨平台应用程序的面向对象的程序设计语言。Java 技术具有卓越的通用性、高效性、平台移植性和安全性，广泛应用于PC、数据中心、游戏控制台、科学超级计算机、移动电话和互联网，同时拥有全球最大的开发者专业社群。','java','upload/java_68srL3X.jpg'),(4,'Python','诸葛亮','Python具有丰富和强大的库。它常被昵称为胶水语言，能够把用其他语言制作的各种模块（尤其是C/C++）很轻松地联结在一起。常见的一种应用情形是，使用Python快速生成程序的原型（有时甚至是程序的最终界面），然后对其中有特别要求的部分，用更合适的语言改写，比如3D游戏中的图形渲染模块，性能要求特别高，就可以用C/C++重写，而后封装为Python可以调用的扩展类库。需要注意的是在您使用扩展类库时可能需要考虑平台问题，某些可能不提供跨平台的实现。','python','upload/python.png');
/*!40000 ALTER TABLE `wechat_academyinfo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `wechat_classinfo`
--

LOCK TABLES `wechat_classinfo` WRITE;
/*!40000 ALTER TABLE `wechat_classinfo` DISABLE KEYS */;
INSERT INTO `wechat_classinfo` VALUES (1,'0810基础班','2015-08-10','吕东雪',1,'0810'),(2,'0910就业班','2015-09-10','吕东雪',1,'0910');
/*!40000 ALTER TABLE `wechat_classinfo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `wechat_gradeinfo`
--

LOCK TABLES `wechat_studentinfo` WRITE;
/*!40000 ALTER TABLE `wechat_studentinfo` DISABLE KEYS */;
INSERT INTO `wechat_studentinfo` VALUES (1,'ohfZct5JajFvfUtzDPIijzn8gI0E',1,'细水长流',1,'邓佳佳','13520322335','2894220','2894220@qq.com','150426199105220034','http://wx.qlogo.cn/mmopen/w3Uk3hmiadlRwibEbtlzAh4O3CXYJQHop7CEaBHIyGkSQJdlSiceo7jA4y1J03sWgmn85AkibuEHT8S2wULibyc1CFUlDPIIEmPGN/96','2015-09-15','2015-09-15',1),(2,'ohfZct259RmDsQ4YqpXPEEvfIv-o',1,'Victory',1,'李志威','13854612784','329396703','329396703@qq.com','150293827182829191','http://wx.qlogo.cn/mmopen/eLD4PeJmVfwmsZWictfbPo5dChPZybMuNFt0FMpw4pHMKRWWrLpWvqfZJ7m39LPIS8faRhxGqe1OpZVMYHBjugfOa6FV59gop/96','2015-09-15','2015-09-15',1),(3,'ohfZct2kB8WudugdTBKek3N0XzRs',1,'邻家大叔',1,'刘鑫','13510948163','101010','101010@qq.com','150293827182829191','http://wx.qlogo.cn/mmopen/wjVtTPhRGGibBxpOn1flNWvYJf8TjFjxdWRxknadqjB2ibNAwniaGloicEaD5X94r0ow6MyiaPGSnaQKkjJcdiaviaa9CxCLj8lLenp/96','2015-09-15','2015-09-15',1),(4,'ohfZct-nXop1QTYQb7UJ4X3sstHI',1,'蓝蜻蜓',1,'薄龙飞','13845726421','101010','101010@qq.com','150293827182829191','http://wx.qlogo.cn/mmopen/wjVtTPhRGG8DwwMVcJ6F2JX2zZic6lJzicsAAOGB8vtTl5W1mvaHNKn4kHDalKMBiaiaLwlkibg9mHzAnxgwtnQwibBsf1LOhzYNle/96','2015-09-15','2015-09-15',1),(5,'ohfZct6p6Ra7MZamGN207Zs_si-s',1,'柳叶',0,'老师','13584642131','101010','101010@qq.com','150293827182829191','http://wx.qlogo.cn/mmopen/w3Uk3hmiadlRwibEbtlzAh4P6Kn6B66Nl5ELBbanKMhZ7fUT5AR9IoboJNqcSDiacHf1SbYW641fQgLJhnC90icSkQxQ7fmtpGSE/96','2015-09-15','2015-09-15',1),(6,'ohfZct8KlIai5kugEvrVc5JJ1vZw',1,'似乎没有对错',1,'啊啊啊','123','101010','101010@qq.com','150293827182829191','http://wx.qlogo.cn/mmopen/PiajxSqBRaEJwW1o0eicanycT7HcYPPsZnFfh6Q27ibfq9hQM65GerporQ9WWnyqsFcDszBibiaU2siag1rIBicW6Gfpw/96','2015-09-15','2015-09-15',1),(7,'ohfZct2mA657PYbeP7OtIy1rv8ck',0,'小鹏',1,'邢文鹏','18611198863','','','','http://wx.qlogo.cn/mmopen/ajNVdqHZLLAQBJEWagT5icPzvRRsMp4trY0dZ9DClKQ0ESPfOp3eQc0pjDoeopflGf8tOYBWZmQZfy3T4RiadltA/96','2015-09-15','2015-09-15',1);
/*!40000 ALTER TABLE `wechat_studentinfo` ENABLE KEYS */;
UNLOCK TABLES;

LOCK TABLES `wechat_syllabusinfo` WRITE;
/*!40000 ALTER TABLE `wechat_syllabusinfo` DISABLE KEYS */;
INSERT INTO `wechat_syllabusinfo` VALUES (1,'C语言提高阶段','配置开发环境\r\nC提高（数据类型、变量、内存四区、指针基础）\r\nC提高（C语言中的字符串、一维数组、二维数组）\r\nC提高（指针数组和数组指针）\r\nC提高（多维数组）\r\nC提高(结构体)\r\nC提高(文件)\r\nC提高(链表)\r\n五一放假\r\n五一放假\r\n五一放假\r\nC提高(动态库的封装和设计)\r\nC综合练习',16,1),(2,'C++基础和进阶','C++基础(C++对C的扩展)\r\nC++基础(C++对C的扩展, 面向过程向面向对象编程转变)\r\nC++基础（构造和析构、静态成员、对象管理)\r\nC++基础（对象动态管理、友元函数、友元类、操作符重载）\r\nC++基础（操作符重载提高）\r\nC++基础（类的继承、多继承、多态）\r\nC++基础多态原理、多态案例）\r\nC++基础（C语言的多态、C多态综合训练）\r\nC++进阶(函数模板、类模板)\r\nC++进阶(类型转换、异常、I/O流)\r\nC++综合练习\r\nC++进阶(STL编程实践)\r\nC++进阶(STL编程实践)',35,1),(3,'数据结构和算法','数据结构（算法基础、链表顺序、链式链式存储、循环链表）\r\n数据结构（双向链表、栈（顺序和链式）、队列（顺序和链式））\r\n数据结构（栈的应用、树基本概念及遍历、二叉树）\r\n数据结构（排序算法、冒泡算法、选择、插入、快速、希尔）\r\n数据结构（C++版本链表、堆、栈及综合复习）',42,1),(4,'设计模式及杂项','C++进阶(设计模式,(单例、工厂、代理、迭代))\r\nC++进阶（设计模式）\r\nC++进阶（设计模式）\r\nC++进阶(C11新特性、boost开发实战)（赠送课程）\r\nC++进阶(boost开发实战)（赠送课程）\r\nC++阶段综合训练\r\n此阶段之前课程C++学院与游戏学院共用',50,1),(5,'Qt跨平台界面开发','跨平台界面开发(QT1基础)\r\n跨平台界面开发(QT2基础)\r\n跨平台界面开发(QT3项目)\r\n跨平台界面开发(QT4项目)\r\n跨平台界面开发(QT5项目)',58,1),(6,'Linux开发基础课程','Unix/Linux操作基础（基本命令，用户管理，安装卸载，网络配置)\r\nUnix/Linux开发基础(vim/gcc,g++编译器,gdb调试工具)\r\n端午节\r\nUnix/Linux项目管理与库管理(makefile编程，共享库，静态库，库版本)\r\nUnix/Linux 文件I/O（文件描述符，文件读写）\r\nUnix/Linux文件系统和目录操作\r\nUnix/Linux进程（创建，回收，进程状态）\r\nUnix/Linux进程间通信(IPC) 管道以及FIFO MAP操作\r\nUnix/Linux仿真myshell案例',70,1),(7,'Linux开发进阶课程','Unix/Linux进程间关系和守护进程\r\nUnix/Linux阶段综合复习及考试1\r\nUnix/Linux信号\r\nUnix/Linux线程(创建，销毁，回收)\r\nUnix/Linux线程同步机制\r\nUnix/Linux 网络协议基础\r\nUnix/Linux socket网络编程\r\nUnix/Linux socket网络编程\r\nUnix/Linux 并发服务器一（多进程/多线程）\r\nUnix/Linux 并发服务器二（多路I/O复用）\r\nUnix/Linux shell编程\r\nUnix/Linux shell编程\r\nUnix/Linux阶段综合复习及考试2',89,1),(8,'数据库及SQL语句','数据开发(SQl语句)\r\n数据开发(SQl语句)\r\n数据开发(oracle proc开发实战)\r\n数据开发(oracle proc开发实战)\r\n数据开发(mysql开发实战)\r\n数据开发(mysql开发实战)',98,1),(9,'MFC开发','Windows界面开发(Win消息机制 SDK编程基础)\r\nWindows界面开发(MFC类库与常用控件)\r\nWindows界面开发(MFC对话框文档视图)\r\nWindows界面开发(MFC对话框文档视图)\r\nWindows界面开发(MFC Socket编程)\r\nWindows界面开发(MFC 数据库编程)\r\nWindows界面开发(MFC_控件编程)\r\nWindows界面开发(MFC com组件编程)',110,1);
/*!40000 ALTER TABLE `wechat_syllabusinfo` ENABLE KEYS */;
UNLOCK TABLES;
