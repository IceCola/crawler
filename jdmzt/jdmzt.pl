#!/usr/bin/perl
use strict;
use warnings;
use LWP 5.64;               ##载入新版本的LWP classes
use LWP::Simple;
use LWP::UserAgent;
use LWP::ConnCache;
use HTML::TreeBuilder;
use Cwd;
#use Unicode::MapUTF8 qw(to_utf8 from_utf8);
use Digest::MD5 qw(md5 md5_hex md5_base64);
 
my $foreurl="http://jandan.net/ooxx/page-";
my $PAGE=955;
my $cur_page=955;
 
my $browser=LWP::UserAgent->new();                                   ##LWP::UserAgent用来请求页面
$browser->agent('Mozilla/4.0 (compatible; MSIE 5.12; Mac_PowerPC)');##伪装一下
$browser->timeout(10);                                               ##request连接超时为10秒
$browser->protocols_allowed(['http','gopher']);                      ##只接受 http 和 gopher 协议
$browser->conn_cache(LWP::ConnCache->new());
 	my $count=21758;
 		my $picno;
 
while($cur_page <=  $PAGE){
    my $url=$foreurl.$cur_page;
    my $response=$browser->get($url);
    unless ($response->is_success){
        print "无法获取$url -- ",$response->status_line,"\n";
    	$cur_page++;   
        next;
    }
    print "page: $cur_page\n";
     
    my $html=$response->content;
#    $html=to_utf8({-string=>$html,-charset=>'gb2312'});               ##把页面编码从gb2312转为utf8

	my @imgsx;

	$html =~ s/.*<ol(.*?)ol>.*/\1/is ;
	
#	print "html:\n".$html;
	
	while ( $html =~ /pic=(http\S*?jpg)/ig){
		push @imgsx, $1;
	}

	foreach (@imgsx){
		my $src=$_; 
		$picno =sprintf ("%#05s","$count");
		 LWP::Simple::getstore($src,"$picno.jpg")               
        or die "get picture failed! -- $url";                       ##访问页面，直接把内容存为文件
        print "saving $picno..\n";
        $count++;
    }        
    
    $|=1;
    $cur_page++;  
    print "sleeping..   ";   
    sleep(3);
    print "go on now\n";
}