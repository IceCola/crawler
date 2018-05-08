#!/usr/bin/perl
use strict;
use warnings;
use LWP 5.64;               ##�����°汾��LWP classes
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
 
my $browser=LWP::UserAgent->new();                                   ##LWP::UserAgent��������ҳ��
$browser->agent('Mozilla/4.0 (compatible; MSIE 5.12; Mac_PowerPC)');##αװһ��
$browser->timeout(10);                                               ##request���ӳ�ʱΪ10��
$browser->protocols_allowed(['http','gopher']);                      ##ֻ���� http �� gopher Э��
$browser->conn_cache(LWP::ConnCache->new());
 	my $count=21758;
 		my $picno;
 
while($cur_page <=  $PAGE){
    my $url=$foreurl.$cur_page;
    my $response=$browser->get($url);
    unless ($response->is_success){
        print "�޷���ȡ$url -- ",$response->status_line,"\n";
    	$cur_page++;   
        next;
    }
    print "page: $cur_page\n";
     
    my $html=$response->content;
#    $html=to_utf8({-string=>$html,-charset=>'gb2312'});               ##��ҳ������gb2312תΪutf8

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
        or die "get picture failed! -- $url";                       ##����ҳ�棬ֱ�Ӱ����ݴ�Ϊ�ļ�
        print "saving $picno..\n";
        $count++;
    }        
    
    $|=1;
    $cur_page++;  
    print "sleeping..   ";   
    sleep(3);
    print "go on now\n";
}