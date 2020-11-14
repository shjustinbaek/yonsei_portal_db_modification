-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`SUBJECT`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`SUBJECTS` (
  `OpenYear` INT NOT NULL,
  `OpenSem` VARCHAR(45) NOT NULL,
  `G1` VARCHAR(45) NULL,
  `G2` VARCHAR(45) NOT NULL,
  `G3` VARCHAR(45) NOT NULL,
  `SubjectID` VARCHAR(45) NOT NULL,
  `SubjectName` VARCHAR(300) NULL,
  `Credit` FLOAT NULL,
  `SubjectTime` VARCHAR(45) NULL,
  `FullCapa` VARCHAR(45) NULL,
  `1Capa` VARCHAR(45) NULL,
  `2Capa` VARCHAR(45) NULL,
  `3Capa` VARCHAR(45) NULL,
  `4Capa` VARCHAR(45) NULL,
  `MaxMileage` INT NULL,
  `IfExchangeP` VARCHAR(45) NULL,
  `SyllUploadDate` VARCHAR(45) NULL,
  `SyllLastUpdate` VARCHAR(45) NULL,
  `SubjectsFor` TEXT NULL,
  `SubjectGoal` TEXT NULL,
  `Prerequisite` TEXT NULL,
  `SubjectMethod` TEXT NULL,
  `SubjectGP` TEXT NULL,
  `TextBook` TEXT NULL,
  `InfoProf` TEXT NULL,
  `InfoTA` TEXT NULL,
  `EngSyll` TEXT NULL,
  PRIMARY KEY (`OpenYear`, `OpenSem`, `G3`, `SubjectID`, `G2`))
ENGINE = InnoDB CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;


-- -----------------------------------------------------
-- Table `mydb`.`CLASSPROPERTY`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`CLASSPROPERTY` (
  `SUBJECT_OpenYear` INT NOT NULL,
  `SUBJECT_OpenSem` VARCHAR(45) NOT NULL,
  `SUBJECT_G3` VARCHAR(45) NOT NULL,
  `SUBJECT_SubjectID` VARCHAR(45) NOT NULL,
  `SUBJECT_G2` VARCHAR(45) NOT NULL,
  `Property` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`SUBJECT_OpenYear`, `SUBJECT_OpenSem`, `SUBJECT_G3`, `SUBJECT_SubjectID`, `SUBJECT_G2`, `Property`),
  CONSTRAINT `fk_table1_SUBJECT`
    FOREIGN KEY (`SUBJECT_OpenYear` , `SUBJECT_OpenSem` , `SUBJECT_G3` , `SUBJECT_SubjectID` , `SUBJECT_G2`)
    REFERENCES `mydb`.`SUBJECTS` (`OpenYear` , `OpenSem` , `G3` , `SubjectID` , `G2`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;


-- -----------------------------------------------------
-- Table `mydb`.`WEEKLYSYLLABUS`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`WEEKLYSYLLABUS` (
  `SUBJECT_OpenYear` INT NOT NULL,
  `SUBJECT_OpenSem` VARCHAR(45) NOT NULL,
  `SUBJECT_G3` VARCHAR(45) NOT NULL,
  `SUBJECT_SubjectID` VARCHAR(45) NOT NULL,
  `SUBJECT_G2` VARCHAR(45) NOT NULL,
  `Week` VARCHAR(45) NOT NULL,
  `DatePeriod` VARCHAR(45) NULL,
  `Content` TEXT NULL,
  `Event` TEXT NULL,
  `Remarks` TEXT NULL,
  PRIMARY KEY (`SUBJECT_OpenYear`, `SUBJECT_OpenSem`, `SUBJECT_G3`, `SUBJECT_SubjectID`, `SUBJECT_G2`, `Week`),
  CONSTRAINT `fk_table2_SUBJECT1`
    FOREIGN KEY (`SUBJECT_OpenYear` , `SUBJECT_OpenSem` , `SUBJECT_G3` , `SUBJECT_SubjectID` , `SUBJECT_G2`)
    REFERENCES `mydb`.`SUBJECTS` (`OpenYear` , `OpenSem` , `G3` , `SubjectID` , `G2`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;


-- -----------------------------------------------------
-- Table `mydb`.`BUILDING`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`BUILDING` (
  `BuildingName` VARCHAR(45) NOT NULL,
  `Coordinate` VARCHAR(45) NULL,
  `AbbreviatedAs` VARCHAR(45) NULL,
  PRIMARY KEY (`BuildingName`))
ENGINE = InnoDB CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;


-- -----------------------------------------------------
-- Table `mydb`.`PROFESSOR`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`PROFESSOR` (
  `ProfName` VARCHAR(100) NOT NULL,
  `Department` VARCHAR(100) NOT NULL,
  `OfficeNumber` VARCHAR(100) NULL,
  `Phone` VARCHAR(100) NULL,
  `Email` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`ProfName`, `Department`,`Email`))
ENGINE = InnoDB CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;


-- -----------------------------------------------------
-- Table `mydb`.`SUBJECT/PROFESSOR`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`SUBJECTS_PROFESSOR` (
  `SUBJECT_OpenYear` INT NOT NULL,
  `SUBJECT_OpenSem` VARCHAR(45) NOT NULL,
  `SUBJECT_G3` VARCHAR(45) NOT NULL,
  `SUBJECT_SubjectID` VARCHAR(45) NOT NULL,
  `SUBJECT_G2` VARCHAR(45) NOT NULL,
  `PROFESSOR_ProfName` VARCHAR(100) NOT NULL,
  `PROFESSOR_Department` VARCHAR(100) NOT NULL,
  `PROFESSOR_Email` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`SUBJECT_OpenYear`, `SUBJECT_OpenSem`, `SUBJECT_G3`, `SUBJECT_SubjectID`, `SUBJECT_G2`, `PROFESSOR_ProfName`, `PROFESSOR_Department`,`PROFESSOR_Email`),
  INDEX `fk_SUBJECTS_PROFESSOR_PROFESSOR1_idx` (`PROFESSOR_ProfName` ASC, `PROFESSOR_Department` ASC, `PROFESSOR_Email` ASC) VISIBLE,
  CONSTRAINT `fk_table3_SUBJECTS1`
    FOREIGN KEY (`SUBJECT_OpenYear` , `SUBJECT_OpenSem` , `SUBJECT_G3` , `SUBJECT_SubjectID` , `SUBJECT_G2`)
    REFERENCES `mydb`.`SUBJECTS` (`OpenYear` , `OpenSem` , `G3` , `SubjectID` , `G2`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_SUBJECTS_PROFESSOR_PROFESSOR1`
    FOREIGN KEY (`PROFESSOR_ProfName` , `PROFESSOR_Department`)
    REFERENCES `mydb`.`PROFESSOR` (`ProfName` , `Department`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;


-- -----------------------------------------------------
-- Table `mydb`.`SUBJECT/BUILDING`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`SUBJECTS_BUILDING` (
  `SUBJECT_OpenYear` INT NOT NULL,
  `SUBJECT_OpenSem` VARCHAR(45) NOT NULL,
  `SUBJECT_G3` VARCHAR(45) NOT NULL,
  `SUBJECT_SubjectID` VARCHAR(45) NOT NULL,
  `SUBJECT_G2` VARCHAR(45) NOT NULL,
  `BUILDING_BuildingName` VARCHAR(45) NOT NULL,
  `RoomNum` VARCHAR(45) NULL,
  PRIMARY KEY (`SUBJECT_OpenYear`, `SUBJECT_OpenSem`, `SUBJECT_G3`, `SUBJECT_SubjectID`, `SUBJECT_G2`, `BUILDING_BuildingName`),
  INDEX `fk_SUBJECT/BUILDING_BUILDING1_idx` (`BUILDING_BuildingName` ASC) VISIBLE,
  CONSTRAINT `fk_table6_SUBJECT1`
    FOREIGN KEY (`SUBJECT_OpenYear` , `SUBJECT_OpenSem` , `SUBJECT_G3` , `SUBJECT_SubjectID` , `SUBJECT_G2`)
    REFERENCES `mydb`.`SUBJECTS` (`OpenYear` , `OpenSem` , `G3` , `SubjectID` , `G2`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_SUBJECT_BUILDING_BUILDING1`
    FOREIGN KEY (`BUILDING_BuildingName`)
    REFERENCES `mydb`.`BUILDING` (`BuildingName`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;


-- -----------------------------------------------------
-- Table `mydb`.`MAJOR`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`MAJOR` (
  `MajorID` VARCHAR(45) NOT NULL,
  `MajorName` VARCHAR(45) NULL,
  PRIMARY KEY (`MajorID`))
ENGINE = InnoDB CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;


-- -----------------------------------------------------
-- Table `mydb`.`STUDENT`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`STUDENT` (
  `StudentID` VARCHAR(20) NOT NULL,
  `IfGraduating` VARCHAR(45) NULL,
  `SchoolYear` VARCHAR(45) NULL,
  `MAJOR_MajorID` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`StudentID`),
  INDEX `fk_STUDENT_MAJOR1_idx` (`MAJOR_MajorID` ASC) VISIBLE,
  CONSTRAINT `fk_STUDENT_MAJOR1`
    FOREIGN KEY (`MAJOR_MajorID`)
    REFERENCES `mydb`.`MAJOR` (`MajorID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;


-- -----------------------------------------------------
-- Table `mydb`.`FINISHEDSUBJECT`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`FINISHEDSUBJECT` (
  `SUBJECT_OpenYear` INT NOT NULL,
  `SUBJECT_OpenSem` VARCHAR(45) NOT NULL,
  `SUBJECT_G3` VARCHAR(45) NOT NULL,
  `SUBJECT_SubjectID` VARCHAR(45) NOT NULL,
  `SUBJECT_G2` VARCHAR(45) NOT NULL,
  `Grade` VARCHAR(45) NULL,
  `STUDENT_StudentID` VARCHAR(20) NOT NULL,
  PRIMARY KEY (`SUBJECT_OpenYear`, `SUBJECT_OpenSem`, `SUBJECT_G3`, `SUBJECT_SubjectID`, `SUBJECT_G2`, `STUDENT_StudentID`),
  INDEX `fk_FINISHEDSUBJECT_STUDENT1_idx` (`STUDENT_StudentID` ASC) VISIBLE,
  CONSTRAINT `fk_table7_SUBJECTS1`
    FOREIGN KEY (`SUBJECT_OpenYear` , `SUBJECT_OpenSem` , `SUBJECT_G3` , `SUBJECT_SubjectID` , `SUBJECT_G2`)
    REFERENCES `mydb`.`SUBJECTS` (`OpenYear` , `OpenSem` , `G3` , `SubjectID` , `G2`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_FINISHEDSUBJECT_STUDENT1`
    FOREIGN KEY (`STUDENT_StudentID`)
    REFERENCES `mydb`.`STUDENT` (`StudentID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;


-- -----------------------------------------------------
-- Table `mydb`.`GRADREQSPEC`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`GRADREQSPEC` (
  `MAJOR_MajorID` VARCHAR(45) NOT NULL,
  `SpecID` VARCHAR(45) NOT NULL,
  `Req` VARCHAR(45) NULL,
  `NumCreditReq` VARCHAR(45) NULL,
  INDEX `fk_table8_MAJOR1_idx` (`MAJOR_MajorID` ASC) VISIBLE,
  PRIMARY KEY (`SpecID`),
  CONSTRAINT `fk_table8_MAJOR1`
    FOREIGN KEY (`MAJOR_MajorID`)
    REFERENCES `mydb`.`MAJOR` (`MajorID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;


-- -----------------------------------------------------
-- Table `mydb`.`GRADREQTREE`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`GRADREQTREE` (
  `Left` VARCHAR(45) NOT NULL,
  `Right` VARCHAR(45) NULL,
  `Depth` VARCHAR(45) NULL,
  `NodeName` VARCHAR(45) NULL,
  PRIMARY KEY (`Left`))
ENGINE = InnoDB CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;


-- -----------------------------------------------------
-- Table `mydb`.`APPLIEDSUBJECT`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`APPLIEDSUBJECT` (
  `SUBJECT_OpenYear` INT NOT NULL,
  `SUBJECT_OpenSem` VARCHAR(45) NOT NULL,
  `SUBJECT_G3` VARCHAR(45) NOT NULL,
  `SUBJECT_SubjectID` VARCHAR(45) NOT NULL,
  `SUBJECT_G2` VARCHAR(45) NOT NULL,
  `MileageBet` VARCHAR(45) NULL,
  `IfEnrolled` VARCHAR(45) NULL,
  `STUDENT_StudentID` VARCHAR(20) NOT NULL,
  PRIMARY KEY (`SUBJECT_OpenYear`, `SUBJECT_OpenSem`, `SUBJECT_G3`, `SUBJECT_SubjectID`, `SUBJECT_G2`, `STUDENT_StudentID`),
  INDEX `fk_APPLIEDSUBJECT_STUDENT1_idx` (`STUDENT_StudentID` ASC) VISIBLE,
  CONSTRAINT `fk_table10_SUBJECT1`
    FOREIGN KEY (`SUBJECT_OpenYear` , `SUBJECT_OpenSem` , `SUBJECT_G3` , `SUBJECT_SubjectID` , `SUBJECT_G2`)
    REFERENCES `mydb`.`SUBJECTS` (`OpenYear` , `OpenSem` , `G3` , `SubjectID` , `G2`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_APPLIEDSUBJECT_STUDENT1`
    FOREIGN KEY (`STUDENT_StudentID`)
    REFERENCES `mydb`.`STUDENT` (`StudentID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;



