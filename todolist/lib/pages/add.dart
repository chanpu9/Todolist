import 'package:flutter/material.dart';
// http method package
import 'package:http/http.dart' as http;
import 'dart:async';
import 'dart:convert';

class AddPage extends StatefulWidget {
  AddPage({Key? key}) : super(key: key);

  @override
  _AddPageState createState() => _AddPageState();
}

class _AddPageState extends State<AddPage> {
  TextEditingController todo_title = TextEditingController();
  TextEditingController todo_detail = TextEditingController();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('เพิ่มรายการใหม่'),),
      body: Padding(
        padding: const EdgeInsets.all(20.0),
        child: ListView(
          children: [
            // ช่องกรอกข้อมูล Title
            TextField(
              controller: todo_title,
              decoration: InputDecoration(
                  labelText: 'รายการที่ต้องทำ',
                  border: OutlineInputBorder())
            ),
            SizedBox(height: 30,),
            TextField(
              minLines: 4,
              maxLines: 8,
              controller: todo_detail,
              decoration: InputDecoration(
                  labelText: ' รายละเอียด',
                  border: OutlineInputBorder())
            ),
            SizedBox(height: 30,),
            // ปุ่มเพิ่มข้อมูล
            Padding(
              padding: const EdgeInsets.all(20.0),
              child: ElevatedButton(
                onPressed: () {
                  print('----------');
                  print('title: ${todo_title.text}');
                  print('detail: ${todo_detail.text}');
                  postToDo();
                  // ฟังก์ชันสำหรับ refresh หน้า
                  setState(() {
                    todo_title.clear();
                    todo_detail.clear();
                  });
                },
                child: Text("เพิ่มรายการ"),
                style: ButtonStyle(
                    backgroundColor:
                        MaterialStateProperty.all(Colors.blue),
                    padding: MaterialStateProperty.all(
                        EdgeInsets.fromLTRB(50, 20, 50, 20)),
                    textStyle:
                        MaterialStateProperty.all(TextStyle(fontSize: 30))),
              ),
            ),
          ]
        ),
      ),
    );
  }

  Future postToDo() async {
    //var url = Uri.https('d488-27-55-76-36.ngrok.io', '/api/create-todolist/');
    var url = Uri.http('192.168.62.121:8000', '/api/create-todolist/');
    Map<String, String> header = {"Content-type":"application/json"};
    String jsondata = '{"title":"${todo_title.text}", "detail":"${todo_detail.text}"}';
    var response = await http.post(url, headers: header, body: jsondata);
    print('------result------');
    print(response.body);
  }

}