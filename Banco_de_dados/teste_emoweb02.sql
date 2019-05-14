/*
Navicat MySQL Data Transfer

Source Server         : BD
Source Server Version : 50714
Source Host           : localhost:3306
Source Database       : teste_emoweb

Target Server Type    : MYSQL
Target Server Version : 50714
File Encoding         : 65001

Date: 2019-05-14 10:00:02
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for dadosemocao
-- ----------------------------
DROP TABLE IF EXISTS `dadosemocao`;
CREATE TABLE `dadosemocao` (
  `ID_Emocao` int(11) NOT NULL AUTO_INCREMENT,
  `alegria` int(11) DEFAULT NULL,
  `tristeza` int(11) DEFAULT NULL,
  `desgosto` int(11) DEFAULT NULL,
  `desprezo` int(11) DEFAULT NULL,
  `raiva` int(11) DEFAULT NULL,
  `medo` int(11) DEFAULT NULL,
  `surpresa` int(11) DEFAULT NULL,
  `valencia` int(11) DEFAULT NULL,
  `engajamento` int(11) DEFAULT NULL,
  `tempo` varchar(11) DEFAULT NULL,
  `horas` varchar(50) DEFAULT NULL,
  `ID_Site` int(11) NOT NULL,
  `ID_Usuario` int(11) NOT NULL,
  `ID_Sessao` int(11) NOT NULL,
  PRIMARY KEY (`ID_Emocao`,`ID_Site`,`ID_Usuario`,`ID_Sessao`),
  UNIQUE KEY `IdEmocao` (`ID_Emocao`),
  KEY `ID_filmes` (`ID_Site`),
  KEY `Id_usuario` (`ID_Usuario`),
  KEY `ID_Sessao` (`ID_Sessao`),
  CONSTRAINT `dadosemocao_ibfk_1` FOREIGN KEY (`ID_Site`) REFERENCES `site` (`ID_Site`),
  CONSTRAINT `dadosemocao_ibfk_2` FOREIGN KEY (`ID_Usuario`) REFERENCES `usuario` (`ID_Usuario`),
  CONSTRAINT `dadosemocao_ibfk_3` FOREIGN KEY (`ID_Sessao`) REFERENCES `sessao` (`ID_Sessao`)
) ENGINE=InnoDB AUTO_INCREMENT=507287 DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of dadosemocao
-- ----------------------------

-- ----------------------------
-- Table structure for dados_sensores
-- ----------------------------
DROP TABLE IF EXISTS `dados_sensores`;
CREATE TABLE `dados_sensores` (
  `ID_Sensores` int(11) NOT NULL AUTO_INCREMENT,
  `Horas` varchar(30) DEFAULT NULL,
  `Cont` varchar(255) DEFAULT NULL,
  `ID_Site` int(11) NOT NULL,
  `ID_Sessao` int(11) NOT NULL,
  `tempoinicio` varchar(255) DEFAULT NULL,
  `Id_Usuario` int(11) NOT NULL,
  `attention` varchar(30) DEFAULT NULL,
  `meditation` varchar(30) DEFAULT NULL,
  `rawValue` varchar(30) DEFAULT NULL,
  `theta` varchar(30) DEFAULT NULL,
  `delta` varchar(20) DEFAULT NULL,
  `lowAlpha` varchar(30) DEFAULT NULL,
  `highAlpha` varchar(30) DEFAULT NULL,
  `lowBeta` varchar(30) DEFAULT NULL,
  `highBeta` varchar(30) DEFAULT NULL,
  `lowGamma` varchar(30) DEFAULT NULL,
  `midGamma` varchar(30) DEFAULT NULL,
  `poorSignal` varchar(30) DEFAULT NULL,
  `blinkStrength` varchar(30) DEFAULT NULL,
  `gsr` varchar(30) DEFAULT NULL,
  `ecg` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`ID_Sensores`,`ID_Site`,`Id_Usuario`,`ID_Sessao`),
  KEY `ID_filmes` (`ID_Site`),
  KEY `Id_usuario` (`Id_Usuario`),
  KEY `ID_Sessao` (`ID_Sessao`),
  CONSTRAINT `dados_sensores_ibfk_1` FOREIGN KEY (`ID_Site`) REFERENCES `site` (`ID_Site`),
  CONSTRAINT `dados_sensores_ibfk_2` FOREIGN KEY (`Id_Usuario`) REFERENCES `usuario` (`ID_Usuario`),
  CONSTRAINT `dados_sensores_ibfk_3` FOREIGN KEY (`ID_Sessao`) REFERENCES `sessao` (`ID_Sessao`)
) ENGINE=InnoDB AUTO_INCREMENT=780453 DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of dados_sensores
-- ----------------------------

-- ----------------------------
-- Table structure for sessao
-- ----------------------------
DROP TABLE IF EXISTS `sessao`;
CREATE TABLE `sessao` (
  `ID_Sessao` int(11) NOT NULL AUTO_INCREMENT,
  `Nome_Categoria` varchar(200) DEFAULT NULL,
  `descricao` varchar(250) DEFAULT NULL,
  PRIMARY KEY (`ID_Sessao`),
  UNIQUE KEY `ID_Sessao` (`ID_Sessao`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of sessao
-- ----------------------------

-- ----------------------------
-- Table structure for site
-- ----------------------------
DROP TABLE IF EXISTS `site`;
CREATE TABLE `site` (
  `ID_Site` int(11) NOT NULL AUTO_INCREMENT,
  `Nome_Site` varchar(200) DEFAULT NULL,
  `Descricao` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`ID_Site`)
) ENGINE=InnoDB AUTO_INCREMENT=103 DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of site
-- ----------------------------

-- ----------------------------
-- Table structure for usuario
-- ----------------------------
DROP TABLE IF EXISTS `usuario`;
CREATE TABLE `usuario` (
  `ID_Usuario` int(11) NOT NULL AUTO_INCREMENT,
  `Numero_usuario` int(11) NOT NULL,
  PRIMARY KEY (`ID_Usuario`),
  UNIQUE KEY `Id_usuario` (`ID_Usuario`)
) ENGINE=InnoDB AUTO_INCREMENT=102 DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of usuario
-- ----------------------------
