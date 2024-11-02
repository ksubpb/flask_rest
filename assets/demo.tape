Output demo.gif

Require curl

Set Shell "bash"
Set FontSize 24
Set Width 1200
Set Height 600

Type "curl http://localhost:5001/zipcode/1000001"
Sleep 500ms
Type "  # 100-0001 を検索する"
Sleep 500ms
Enter
Sleep 3s
Type "curl http://localhost:5001/zipcode/prefs/"
Sleep 500ms
Type "東京都"
Sleep 500ms
Type " # 東京都の郵便番号一覧を調べる"
Sleep 500ms
Enter
Sleep 3s
Type "curl -i http://localhost:5001/zipcode/1000001"
Sleep 500ms
Type "  # レスポンスヘッダも表示するようにする．"
Sleep 500ms
Enter
Sleep 3s
Type "curl -i http://localhost:5001/zipcode/1000001"
Sleep 500ms
Type " -X DELETE"
Sleep 500ms
Type "  # 削除する"
Sleep 500ms
Enter
Type "curl -i http://localhost:5001/zipcode/1000001 -X DELETE"
Sleep 500ms
Type "  # 何度実行しても結果は同じ．"
Sleep 500ms
Enter
Sleep 3s
Type "curl http://localhost:5001/zipcode/1000001"
Sleep 500ms
Type "  # 削除したので，100-0001 は見つからない．"
Sleep 500ms
Enter
Sleep 3s
Type "# 100-0001 を登録し直すことにする．"
Sleep 500ms
Enter
Sleep 3s
Type "curl http://localhost:5001/zipcode/1000001"
Sleep 500ms
Type " -X POST"
Sleep 500ms
Type " -d '{"
Type '  "address": "千代田区千代田",'
Enter
Type '  "address_yomi": "チヨダクチヨダ",'
Enter
Type '  "pref": "東京都",'
Enter
Type '  "zipcode": 1000001'
Enter
Type "}'"
Sleep 500ms
Type " -H 'Content-Type: application/json'"
Sleep 500ms
Type "  # curl で JSON を POST メソッドで送るとき，Content-Type の指定が必要．"
Sleep 500ms
Enter
Sleep 3s
Type "curl http://localhost:5001/zipcode/1000001"
Sleep 500ms
Type "  # 登録し直したので，今度は見つかる．"
Sleep 500ms
Enter
Type "  # 再度同じ情報を登録しようとすると，エラーになる．"
Sleep 500ms
Enter

Type "curl http://localhost:5001/zipcode/1000001 -X POST -H 'Content-Type: application/json' "
Sleep 500ms
Type " -d '"
Type '{ "address": "千代田区千代田", "address_yomi": "チヨダクチヨダ", "pref": "東京都", "zipcode": 1000001 }'
Type "'"
Sleep 500ms
Enter
Sleep 3s
Ctrl+D
