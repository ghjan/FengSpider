for (( pn=1; pn<=100; pn=pn+1 )); do

	for ssd in "Python" "angular" "golang" "区块链"

	do 

	curl 'https://www.lagou.com/jobs/positionAjax.json?px=new&city=%E4%B8%8A%E6%B5%B7&needAddtionalResult=false' -H 'Cookie: JSESSIONID=ABAAABAABEEAAJA9DBB4F5BE13CB68F1929E05076AA5976; user_trace_token=20180911093546-ea2b5f08-bc36-4a8b-92ea-3c8aa4ac96fc; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1536629748; _ga=GA1.2.526097846.1536629748; _gat=1; LGSID=20180911093547-01e5fb9f-b563-11e8-8e34-525400f775ce; PRE_UTM=; PRE_HOST=blog.csdn.net; PRE_SITE=https%3A%2F%2Fblog.csdn.net%2Fu012689336%2Farticle%2Fdetails%2F53170371; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Fjobs%2Flist_iOS%3Fpx%3Dnew%26city%3D%25E5%258C%2597%25E4%25BA%25AC; LGUID=20180911093547-01e5fe02-b563-11e8-8e34-525400f775ce; _gid=GA1.2.1306194661.1536629749; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1536629762; LGRID=20180911093601-0a636e7a-b563-11e8-8e34-525400f775ce; SEARCH_ID=8336a78dc3dc41f39a2d083a8a9967ad' -H 'Origin: https://www.lagou.com' -H 'X-Anit-Forge-Code: 0' -H 'Accept-Language: zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7' -H 'X-Requested-With: XMLHttpRequest' -H 'Accept-Encoding: gzip, deflate, br' -H 'Connection: keep-alive' -H 'Pragma: no-cache' -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36' -H 'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' -H 'Accept: application/json, text/javascript, */*; q=0.01' -H 'Cache-Control: no-cache' -H 'Referer: https://www.lagou.com/jobs/list_iOS?px=new&city=%E4%B8%8A%E6%B5%B7' -H 'X-Anit-Forge-Token: None' --data "first=true&pn=1&kd=$ssd" --compressed  > $ssd\_$pn.json


	done
done