from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import serializers, status
from .serializers import TodolistSerializer
from .models import Todolist

# GET Data
@api_view(['GET'])                                  # Decorator ทำให้ api ทำอะไรได้บ้าง
def view_todolist(request):
    alltodolist = Todolist.objects.all()            # ดึงข้อมูลจาก model Todolist == "SELECT * FROM ..."
    serializer = TodolistSerializer(alltodolist, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

# POST Data
@api_view(['POST'])
def create_todolist(request):
    if request.method == 'POST':
        serializer = TodolistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
def update_todolist(request, TID):
    # localhost:8000/api/update-todolist/13
    todo = Todolist.objects.get(id=TID)

    if request.method == 'PUT':
        data = {}
        serializer = TodolistSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            data['status'] = 'updated'
            return Response(data=data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_todolist(request, TID):
    todo = Todolist.objects.get(id=TID)

    if request.method == 'DELETE':
        delete = todo.delete()
        data = {}
        if delete:
            data['status'] = 'deleted'
            statuscode = status.HTTP_200_OK
        else:
            data['status'] = 'failed'
            statuscode = status.HTTP_400_BAD_REQUEST

        return Response(data=data, status=statuscode)


data = [
    {
        "title" : "คอมพิวเตอร์คืออะไร ?",
        "subtitle" : "คอมพิวเตอร์ คือ อุปกรณ์ที่ใช้สำหรับการคำนวณและทำงานอื่น ๆ",
        "image_url" : "https://raw.githubusercontent.com/chanpu9/SampleAPI/main/computer.jpeg",
        "detail" : "คอมพิวเตอร์ (อังกฤษ: computer) หรือศัพท์บัญญัติราชบัณฑิตยสภาว่า คณิตกรณ์ เป็นเครื่องจักรแบบสั่งการได้ที่ออกแบบมาเพื่อดำเนินการกับลำดับตัวดำเนินการทางตรรกศาสตร์หรือคณิตศาสตร์ โดยอนุกรมนี้อาจเปลี่ยนแปลงได้เมื่อพร้อม ส่งผลให้คอมพิวเตอร์สามารถแก้ปัญหาได้มากมาย\n\nคอมพิวเตอร์ถูกประดิษฐ์ออกมาให้ประกอบไปด้วยความจำรูปแบบต่าง ๆ เพื่อเก็บข้อมูล อย่างน้อยหนึ่งส่วนที่มีหน้าที่ดำเนินการคำนวณเกี่ยวกับตัวดำเนินการทางตรรกศาสตร์ และตัวดำเนินการทางคณิตศาสตร์ และส่วนควบคุมที่ใช้เปลี่ยนแปลงลำดับของตัวดำเนินการโดยยึดสารสนเทศที่ถูกเก็บไว้เป็นหลัก อุปกรณ์เหล่านี้จะยอมให้นำเข้าข้อมูลจากแหล่งภายนอก และส่งผลจากการคำนวณตัวดำเนินการออกไป"
    },
    {
        "title" : "มาเขียนโปรแกรมกัน",
        "subtitle" : "บทความนี้จะแนะนำการเร่ิมต้นเชียนโปรแกรม",
        "image_url" : "https://raw.githubusercontent.com/chanpu9/SampleAPI/main/coding.jpeg",
        "detail" : "การเขียนโปรแกรมคอมพิวเตอร์ (อังกฤษ: Computer programming) หรือเรียกให้สั้นลงว่า การเขียนโปรแกรม (อังกฤษ: Programming) หรือ การเขียนโค้ด (Coding) เป็นขั้นตอนการเขียน ทดสอบ และดูแลซอร์สโค้ดของโปรแกรมคอมพิวเตอร์ ซึ่งซอร์สโค้ดนั้นจะเขียนด้วยภาษาโปรแกรม ขั้นตอนการเขียนโปรแกรมต้องการความรู้ในหลายด้านด้วยกัน เกี่ยวกับโปรแกรมที่ต้องการจะเขียน และขั้นตอนวิธีที่จะใช้ ซึ่งในวิศวกรรมซอฟต์แวร์นั้น การเขียนโปรแกรมถือเป็นเพียงขั้นหนึ่งในวงจรชีวิตของการพัฒนาซอฟต์แวร์\n\nการเขียนโปรแกรมจะได้มาซึ่งซอร์สโค้ดของโปรแกรมนั้นๆ โดยปกติแล้วจะอยู่ในรูปแบบของ ข้อความธรรมดา ซึ่งไม่สามารถนำไปใช้งานได้ จะต้องผ่านการคอมไพล์ตัวซอร์สโค้ดนั้นให้เป็นภาษาเครื่อง (Machine Language) เสียก่อนจึงจะได้เป็นโปรแกรมที่พร้อมใช้งาน"
    },
    {
        "title" : "Flutter คืออะไร ?",
        "subtitle" : "Tools สำหรับออกแบบ UI ของ Google",
        "image_url" : "https://raw.githubusercontent.com/chanpu9/SampleAPI/main/mobile.jpg",
        "detail" : "Flutter คือ Framework ที่ใช้สร้าง UI สำหรับ mobile application ที่สามารถทำงานข้ามแพลตฟอร์มได้ทั้ง iOS และ Android ในเวลาเดียวกัน โดยภาษาที่ใช้ใน Flutter นั้นจะเป็นภาษา dart ซึ่งถูกพัฒนาโดย Google และที่สำคัญคือเป็น open source ที่สามารถใช้งานได้แบบฟรี ๆ"
    },
    {
        "title" : "Python คืออะไร ?",
        "subtitle" : "ภาษาเขียนโปรแกรมชนิดหนึ่ง สร้างขึ้นเมื่อ 199X",
        "image_url" : "https://raw.githubusercontent.com/chanpu9/SampleAPI/main/coding.jpeg",
        "detail" : "ภาษาไพทอน (Python programming language) หรือที่มักเรียกกันว่าไพทอน เป็นภาษาระดับสูงซึ่งสร้างโดยคีโด ฟัน โรสซึม โดยเริ่มในปีพ.ศ. 2533 การออกแบบของภาษาไพทอนมุ่งเน้นให้ผู้โปรแกรมสามารถอ่านชุดคำสั่งได้โดยง่ายผ่านการใช้งานอักขระเว้นว่าง (whitespaces) จำนวนมาก นอกจากนั้นการออกแบบภาษาไพทอนและการประยุกต์ใช้แนวคิดการเขียนโปรแกรมเชิงวัตถุในตัวภาษายังช่วยให้นักเขียนโปรแกรมสามารถเขียนโปรแกรมที่เป็นระเบียบ อ่านง่าย มีขนาดเล็ก และง่ายต่อการบำรุง"
    },
    {
        "title" : "Cybersecurity คืออะไร ?",
        "subtitle" : "บทความนี้จะแนะนำเกี่ยวกับความปลอดภัยด้าน IT",
        "image_url" : "https://raw.githubusercontent.com/chanpu9/SampleAPI/main/security.jpeg",
        "detail" : "Cybersecurity เป็นเรื่องที่ว่าด้วยปัญหาด้านความปลอดภัยบนโลกอินเตอร์เน็ต มุ่งเน้นที่ความปลอดภัยในส่วนของ Electronic Data อาทิเช่นการป้องกันการเข้าถึงข้อมูลในรูปแบบของ unauthorized access จากช่องทางอินเตอร์เน็ต, cybercrime การก่ออาชญากรรมทางไซเบอร์โดยมีวัตถุประสงค์ด้านการเงิน, การ hacking และ/หรือ การจารกรรมข้อมูลสำคัญของหน่วยงานต่างๆ หรือแม้กระทั่ง Cyber war การโจมตีสาธารณูประโภคของภาครัฐโดยใช้เครื่องมือทางไซเบอร์พัฒนาเป็นอาวุธในการโจมตี"
    }
]

def Home(request):
    return JsonResponse(data=data, safe=False, json_dumps_params={'ensure_ascii': False})