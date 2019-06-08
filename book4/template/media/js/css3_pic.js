$.fn.css3pic = function(can){
	
	can = $.extend({
					box:null,
                    r_btn:"",
	                content:""
				}, can || {});

$(can.content).find('li').click(function(){
	var dangqian = $(this).attr('class')
	if(dangqian=='on'){
		$(this).animate({'margin-right':'-200px'},500);
		$(this).removeClass('on');
		
		}else{
	$(this).animate({'margin-right':'0'},500).siblings('li').animate({'margin-right':'-200px'},500);
	$(this).addClass('on').siblings('li').removeClass('on');
	
		}
	})
$(can.r_btn).click(function(){
	$(can.content).find('li').removeClass('on');
	$(can.content).find('li').animate({'margin-right':'-200px'},500);
	})

}