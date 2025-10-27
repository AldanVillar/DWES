/*M!999999\- enable the sandbox mode */ 
-- MariaDB dump 10.19  Distrib 10.11.14-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: mysitedb
-- ------------------------------------------------------
-- Server version	10.11.14-MariaDB-0+deb12u2

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `tComentarios`
--

DROP TABLE IF EXISTS `tComentarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `tComentarios` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `comentario` varchar(2000) DEFAULT NULL,
  `usuario_id` int(11) DEFAULT NULL,
  `libro_id` int(11) NOT NULL,
  `fecha` timestamp NULL DEFAULT current_timestamp(),
  PRIMARY KEY (`id`),
  KEY `usuario_id` (`usuario_id`),
  KEY `libro_id` (`libro_id`),
  CONSTRAINT `tComentarios_ibfk_1` FOREIGN KEY (`usuario_id`) REFERENCES `tUsuarios` (`id`),
  CONSTRAINT `tComentarios_ibfk_2` FOREIGN KEY (`libro_id`) REFERENCES `tLibros` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tComentarios`
--

LOCK TABLES `tComentarios` WRITE;
/*!40000 ALTER TABLE `tComentarios` DISABLE KEYS */;
INSERT INTO `tComentarios` VALUES
(1,'Excelente historia',1,1,'2025-10-19 17:21:15'),
(2,'Muy entretenido',2,2,'2025-10-19 17:21:15'),
(3,'Una obra maestra',3,3,'2025-10-19 17:21:15'),
(4,'Recomendado 100%',4,4,'2025-10-19 17:21:15'),
(5,'Un poco largo pero genial',5,5,'2025-10-19 17:21:15'),
(6,'Excelente historia',1,1,'2025-10-19 17:21:15'),
(7,'Muy entretenido',2,2,'2025-10-19 17:21:15'),
(8,'Una obra maestra',3,3,'2025-10-19 17:21:15'),
(9,'Recomendado 100%',4,4,'2025-10-19 17:21:15'),
(10,'Un poco largo pero genial',5,5,'2025-10-19 17:21:15'),
(11,'Tiene una buena historia\r\n',NULL,2,'2025-10-19 17:21:15'),
(12,'Muy recomendado',NULL,1,'2025-10-19 17:30:49');
/*!40000 ALTER TABLE `tComentarios` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tLibros`
--

DROP TABLE IF EXISTS `tLibros`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `tLibros` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) DEFAULT NULL,
  `url_imagen` varchar(200) DEFAULT NULL,
  `autor` varchar(100) DEFAULT NULL,
  `año` year(4) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tLibros`
--

LOCK TABLES `tLibros` WRITE;
/*!40000 ALTER TABLE `tLibros` DISABLE KEYS */;
INSERT INTO `tLibros` VALUES
(1,'1984','https://example.com/1984.jpg','George Orwell',1949),
(2,'El Hobbit','https://example.com/hobbit.jpg','J.R.R. Tolkien',1937),
(3,'Dune','https://example.com/dune.jpg','Frank Herbert',1965),
(4,'Fahrenheit 451','https://example.com/f451.jpg','Ray Bradbury',1953),
(5,'IT','https://example.com/it.jpg','Stephen King',1986),
(6,'1984','https://example.com/1984.jpg','George Orwell',1949),
(7,'El Hobbit','https://example.com/hobbit.jpg','J.R.R. Tolkien',1937),
(8,'Dune','https://example.com/dune.jpg','Frank Herbert',1965),
(9,'Fahrenheit 451','https://example.com/f451.jpg','Ray Bradbury',1953),
(10,'IT','https://example.com/it.jpg','Stephen King',1986);
/*!40000 ALTER TABLE `tLibros` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tUsuarios`
--

DROP TABLE IF EXISTS `tUsuarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `tUsuarios` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) DEFAULT NULL,
  `apellidos` varchar(100) DEFAULT NULL,
  `email` varchar(200) DEFAULT NULL,
  `contraseña` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tUsuarios`
--

LOCK TABLES `tUsuarios` WRITE;
/*!40000 ALTER TABLE `tUsuarios` DISABLE KEYS */;
INSERT INTO `tUsuarios` VALUES
(1,'Laura','Pérez Gómez','laura@mail.com','1234'),
(2,'Carlos','Ruiz Martín','carlos@mail.com','abcd'),
(3,'María','Santos Díaz','maria@mail.com','pass'),
(4,'Pedro','López Gil','pedro@mail.com','clave'),
(5,'Ana','Torres Vega','ana@mail.com','hola');
/*!40000 ALTER TABLE `tUsuarios` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-10-19 19:38:22
