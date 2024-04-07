import configparser
import mysql.connector
from mysql.connector import Error


def getConfig():
    config = configparser.ConfigParser()
    config.read("utilities/properties.ini")
    return config

connect_configure = {
    'user': getConfig()['SQL']['user'],
    'host': getConfig()['SQL']['host'],
    'database':getConfig()['SQL']['database'],
    'password':getConfig()['SQL']['password']
}

def getPassword():
    return 'kjl'

def getconnection():
    try:
        conn = mysql.connector.connect(**connect_configure)
        if conn.is_connected():
            print("connection Successful")
            return conn
    except Error as e:
        print(e)

def getQuery(query):
    conn = getconnection()
    cursor = conn.cursor()
    cursor.execute(query)
    row = cursor.fetchone()
    conn.close()
    return row


