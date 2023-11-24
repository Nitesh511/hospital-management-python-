-- MySQL dump 10.13  Distrib 8.0.22, for Win64 (x86_64)
--
-- Host: localhost    Database: party_info
-- ------------------------------------------------------
-- Server version	8.0.22

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `owner`
--

DROP TABLE IF EXISTS `owner`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `owner` (
  `code` int NOT NULL AUTO_INCREMENT,
  `Code_no` varchar(255) DEFAULT NULL,
  `name` varchar(255) DEFAULT NULL,
  `phone` varchar(255) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  `vat_no` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`code`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `owner`
--

LOCK TABLES `owner` WRITE;
/*!40000 ALTER TABLE `owner` DISABLE KEYS */;
INSERT INTO `owner` VALUES (5,'qew','wqdn','danj','hwdowq','uiw'),(6,'hsoayos','hdoiawhsd9uso','HDIOWAJSJD','UYS08UBW','HSIODJ'),(7,'yghkjl','yguhijk','yfugihj','jkhlj','kj'),(8,'yghkjl','Grocery','yfugihj','jkhlj','kj'),(11,'vat-123','grocery','98766161','ktm','1234567'),(12,'jkwj','wkl','456789','jwdq','56790-2o'),(13,'ghjkl','srdgfhjkhlj','dfhgjkhlj','rsdtfyghlj','fghvjkb'),(14,'rdytfguihoRTDYFUGIHOUI','ghijotyfughij','fguihoj','gxfchjgkh','fghcj'),(15,'ghkjlYJKL','YUGHIJ','UYIH','YGUHI','FYGK'),(16,'ghj','hijl','yguih','vuhij','vj'),(17,'vat-123','grocery','4812936','ktm','5050505'),(18,'ghj','kjh767','67678','67','678'),(19,'vat-1234','aayush','98600000','ktm','43253'),(20,'1','srdgfhjkhlj','dfhgjkhlj','rsdtfyghlj','fghvjkb'),(22,'1234','dk','888','qwk','qla'),(23,'guvhjbk','jbknlm','vjbknl','hbjknl','jlk'),(24,'vbnm,','hjknl','ybkl','gjhkjlk','hjkj'),(25,'yghjklijo;','yjl','ghjbknl','hjkl','ghvjlbk'),(26,'fghjk','fghjbk','dfgh','rtfhgjh','rtyguhil'),(27,'fghjkl','tyguhjl','jklj','hjklj','hjkl'),(28,'ytjklm;,\'','ykl;','ghjknlmGHVJBKNM','hjnlkm;','gh'),(29,'fghjkl;','hbjknlm;,','vhjbknlm','vvhbkjln','fyuig'),(30,'tfyguhTFYGJHKJ','tyfugih','dtfyugih','ygjhk','yugi'),(31,'gjhknlm','ghjbknlm','jkjlk','ghvjhbkjnlk','hjk'),(33,'123Vat','money','8888888','pokha','299832892'),(36,'101','nishant','8621345','KTM','607812');
/*!40000 ALTER TABLE `owner` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-03-12 13:07:42
