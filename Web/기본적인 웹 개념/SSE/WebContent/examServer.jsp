<%@ page language="java" contentType="text/html; charset=EUC-KR"
	pageEncoding="UTF-8"%>
<%@ page import="java.util.Date"%>
<%
	response.setContentType("text/event-stream;charset=UTF-8");
	response.setHeader("Cache-control", "no-cache");
	response.setHeader("Connection", "keep-alive");
	
	System.out.println("----호출----");
	try{
		for(int i=0;i<3;i++){
			Date date = new Date();
						
			out.write("id: " + date.getTime()+"\n" );
			out.write("data; "+ date.toLocaleString() + "\n\n");
			
			out.flush();
			System.out.print(i + " ");
			Thread.currentThread().sleep(3000);
		}
		System.out.println("");
		System.out.println("----한 주기 끝----");
	}catch(InterruptedException e){
		System.out.print("error");
		e.printStackTrace();
	}catch(Exception e){
		System.out.print("error");
	}
	
%>
