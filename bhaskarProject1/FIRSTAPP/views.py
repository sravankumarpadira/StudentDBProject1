from django.shortcuts import render
from django.http import HttpResponse;
# Create your views here.
def hello(request):
    print("hello/uri is requested & helo() is execuate");
    ss = '''
        <html>
            <head>
                <title>hello wedpage</title>
                <style>
                    h1{
                        color:blue;
                        width:80%;
                      }
                    h2{
                        color:red;
                        width:75%;
                        }
                    h3{
                        color:yellow;
                        width:70%;
                    }
                    h1,h2,h3{
                                background-color:black;
                                border:2px solid brown;
                                }
                            </style>
                        <body>
                                <h1>hello idiot......</h1>
                                <hr color='green' width='80%'/>
                                <h2>I need you forever****</h2>
                                <hr color='orange' width='70%'/>
                                <h3>forever is lifetime&&&</h3>
                                <hr color='purple' width='60%'/>
                            </body>
                            </html>
                '''
    return HttpResponse(ss);

import datetime;
def wishes3(request):
    date1=datetime.datetime.now()
    msg1='hello bunny kolbe/****....good';
    hr=int(date1.strftime('%H'));
    imgs='IMG_20210218_104536.jpg'
    if hr<12:
        msg1+='moring!!'
        imgs="IMG_20210218_104536.jpg";
    elif hr<16:
        msg1+='afternoon'
        imgs ='OIP.jpg';
    elif hr<20:
        msg1+='evening'
        imgs="tyg7XAl8oMl2w2BF2KqbERsK0m7.jpg";
    else:
        msg1+='night'
        imgs='tyg7XAl8oMl2w2BF2KqbERsK0m7.jpg'
    dict1={'date1':date1,'msg1':msg1,'imgs':imgs}
    return  render(request,'FirstApp/wishes3.html',dict1);