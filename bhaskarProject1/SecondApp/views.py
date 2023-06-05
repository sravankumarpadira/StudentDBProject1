from django.shortcuts import render
from django.http import HttpResponse;


# Create your views here.
import  time;
def senddatetime(request):
            print('dtime/urp is requested & sendtimetime() is executed');
            ct= time.ctime()
            print('client request date &time on server :: ',ct);
            ss='''
                <html>
                    <head>
                    <title> date-time webpage</title>
                    <style>
                        h1{
                            color:yellow;
                            width:90%;
                            }
                        h2{
                            color:blue;
                            width:75%;
                            }
                          h3{
                              width:60%;
                              }
                    h1,h2,h3{
                                background-color: cyan;
                                border:3px black
                             }
                    </style>
                    </head>
                <body>
                        <center>
                            <h1>heyy potti ****</h1>
                            <hr color="red" width="90%"/>
                            <h2>everyone say's why r you wastetime with you phone</h2>
                            <hr color="red" width="80%"/>
                            <h3> but there didn't no i don't waste time i'm talking with my life partner</h3>
                            <hr color="red" width="70%"/>
                            </center>
                        </body>
                    </html>
                    '''
            return HttpResponse(ss);
