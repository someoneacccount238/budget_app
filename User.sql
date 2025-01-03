CREATE TABLE [dbo].[User]
(
	[Id] INT NOT NULL PRIMARY KEY, 
    [Email] NCHAR(50) NOT NULL, 
    [Password] NCHAR(50) NOT NULL, 
    [MoneySaved] NCHAR(10) NULL
)
