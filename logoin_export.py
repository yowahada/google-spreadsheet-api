# !/usr/bin/env python
# coding:utf-8

from googleapiclient import discovery
import oauth2client
import httplib2
import argparse
import csv
import sys
import urllib
import json
import real_data
from oauth2client import file

#spreadsheet&start position
SPREADSHEET_ID = '1iMgRwd1xPLo4q9JgleCBbOq1W_SPKxBrCcMNishn67Y'
RANGE_NAME = 'A1'
MAJOR_DIMENSTION = 'ROWS'

#鍵とトークン関係の設定
#今回のコードは同一フォルダにclient_secretとcredentialは置いておく
CLIENT_SECRET_FILE = 'client_secret.json'
CREDENTIAL_FILE = "./credential.json"
APPLICATION_NAME = 'CSV Appender'

#認証ファイルの読み込み
store = oauth2client.file.Storage(CREDENTIAL_FILE)
credentials = store.get()

#未認証だった場合は許可を求める(ブラウザ認証)
if not credentials or credentials.invalid:
	SCOPES = 'https://www.googleapis.com/auth/spreadsheets'
	flow = oauth2client.client.flow_from_clientsecrets(CLIENT_SECRET_FILE,SCOPES) #client_secrets.jsonファイルからFlowオブジェクトを生成
	flow.user_agent = APPLICATION_NAME

	#初回認証
	args = '--auth_host_name localhost --logging_level INFO --noauth_local_webserver'
	flags = argparse.ArgumentParser(parents=[oauth2client.tools.argparser]).parse_args(args.split())
	
	credentials = oauth2client.tools.run_flow(flow, store, flags)

# 認証ファイルを使って接続(シートの読み込み)
http = httplib2.Http()
http = credentials.authorize(http)
discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?' 'version=v4')
service = discovery.build('sheets', 'v4', http=http, discoveryServiceUrl=discoveryUrl)
resource = service.spreadsheets().values()

#
parser = argparse.ArgumentParser()
parser.add_argument('infile', nargs='?', type=argparse.FileType('r'), default=sys.stdin)
args = parser.parse_args(sys.argv[1:])

#CSV読み込み
#r = csv.reader(args.infile)
#data = list(r)

#apiから抽出
datas = real_data.Dataget()

#append操作用のボディデータ
body = {
	"range":RANGE_NAME,
	"majorDimension": MAJOR_DIMENSTION,
	"values": datas
}

#スプレッドシートへの書き込み
resource.append(spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME, valueInputOption='USER_ENTERED',body=body).execute()


