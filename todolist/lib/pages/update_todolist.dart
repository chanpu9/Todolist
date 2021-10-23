import 'package:flutter/material.dart';
// http method package
import 'package:http/http.dart' as http;
import 'dart:async';
import 'dart:convert';

class UpdatePage extends StatefulWidget {
  final v1, v2, v3;
  UpdatePage(this.v1, this.v2, this.v3);

  @override
  _UpdatePageState createState() => _UpdatePageState();
}

class _UpdatePageState extends State<UpdatePage> {
  var _v1, _v2, _v3;
  TextEditingController todo_title = TextEditingController();
  TextEditingController todo_detail = TextEditingController();

  @override
  void initState() {
    // TODO: implement initState
    super.initState();
    _v1 = widget.v1; // id
    _v2 = widget.v2; // title
    _v3 = widget.v3; // detail
    todo_title.text = _v2;
    todo_detail.text = _v3;
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('แก้ไขข้อมูล'),
        actions: [
          IconButton(
              onPressed: () {
                print("Delete ID: $_v1");
                deleteToDo();
                // กลับไปหน้าก่อนหน้า
                Navigator.pop(context, 'delete');
              },
              icon: Icon(
                Icons.delete,
                color: Colors.red,
              ))
        ],
      ),
      body: Padding(
        padding: const EdgeInsets.all(20.0),
        child: ListView(children: [
          // ช่องกรอกข้อมูล Title
          TextField(
              controller: todo_title,
              decoration: InputDecoration(
                  labelText: 'รายการที่ต้องทำ', border: OutlineInputBorder())),
          SizedBox(
            height: 30,
          ),
          TextField(
              minLines: 4,
              maxLines: 8,
              controller: todo_detail,
              decoration: InputDecoration(
                  labelText: ' รายละเอียด', border: OutlineInputBorder())),
          SizedBox(
            height: 30,
          ),
          // ปุ่มเพิ่มข้อมูล
          Padding(
            padding: const EdgeInsets.all(20.0),
            child: ElevatedButton(
              onPressed: () {
                print('----------');
                print('title: ${todo_title.text}');
                print('detail: ${todo_detail.text}');
                updateToDo();
                final snackBar = SnackBar(
                  content: const Text('อัปเดตรายการเรียบร้อยแล้ว'),
                );
                ScaffoldMessenger.of(context).showSnackBar(snackBar);
                // // ฟังก์ชันสำหรับ refresh หน้า
                // setState(() {
                //   todo_title.clear();
                //   todo_detail.clear();
                // });
              },
              child: Text("แก้ไข"),
              style: ButtonStyle(
                  backgroundColor: MaterialStateProperty.all(Colors.blue),
                  padding: MaterialStateProperty.all(
                      EdgeInsets.fromLTRB(40, 20, 40, 20)), 
                  textStyle:
                      MaterialStateProperty.all(TextStyle(fontSize: 20))),
            ),
          ),
        ]),
      ),
    );
  }

  Future updateToDo() async {
    // var url = Uri.https('d488-27-55-76-36.ngrok.io', '/api/create-todolist/');
    var url = Uri.http('192.168.62.121:8000', '/api/update-todolist/$_v1');
    Map<String, String> header = {"Content-type": "application/json"};
    String jsondata =
        '{"title":"${todo_title.text}", "detail":"${todo_detail.text}"}';
    var response = await http.put(url, headers: header, body: jsondata);
    print('------result------');
    print(response.body);
  }

  Future deleteToDo() async {
    var url = Uri.http('192.168.62.121:8000', '/api/delete-todolist/$_v1');
    Map<String, String> header = {"Content-type": "application/json"};
    var response = await http.delete(url, headers: header);
    print('------result------');
    print(response.body);
  }
}
