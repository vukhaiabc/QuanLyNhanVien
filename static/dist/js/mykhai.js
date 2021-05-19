
      $('.luuphucap').click(function () { // xử lí thêm mới
        var url = '/qlluongthuong/luuphucap' ;
        var message = 'Thêm mới thành công !' ;
        var errorMes = 'Bản ghi đã có trong CSDL'

        tenpc =  $("input[name=tenpc]").val();
        loaipc = $("input[name=loaipc]").val();
        mucpc = $("input[name=mucpc]").val();
//        var datatest = {};
//        var formdata = $("#themphucap2").serializeArray();
//        console.log(formdata)
//          $.each(formdata, function (i, v) {
//                datatest[v.name] = v.value;
//           });
//            console.log(datatest)


        id = "";
         var datas  = {
	      "tenpc" : tenpc,
	      "loaipc" : loaipc ,
	      "mucpc" : mucpc ,
	      "id" : id
	       }
	      $.ajax({
      url: '/qlluongthuong/luuphucap' ,
      method:'get',
      data:datas,   // JSON.stringify(datas)
      dataType: 'json',
      contentType: "application/json",
      success: function (res) {

       if(res==200) { alert("Thêm mới thành công ! ");window.location.reload()}
       else  alert("Lưu thất bại , phụ cấp đã tồn tại");  //
      },
      error: function (res) {
       console.log(res)
       alert(res)
      }
     });

	});


    function functiontest(e){
        var url = '/qlluongthuong/capnhatphucap' ;
        var message = 'Cập nhật thành công !' ;
        var errorMes = 'Cập nhật thất bại'


          var tenpc,loaipc,mucpc ,id = null ;

          id = $("#capnhatphucap").attr("idphucap") ;

          tenpc =   $("input[name=saveNamePC]").val();
          loaipc = $("input[name=saveTypePC]").val();
          mucpc = $("input[name=saveLevelPC]").val();

	   var datas  = {
	      "tenpc" : tenpc,
	      "loaipc" : loaipc ,
	      "mucpc" : mucpc ,
	      "id" : id
	   }

	  $.ajax({
      url: '/qlluongthuong/capnhatphucap',
      method:'get',
      data:datas,
      dataType: 'json',
      contentType: "application/json",
      success: function (res) {

       if(res==200) { alert(message);window.location.href="/qlluongthuong/qlphucap"}
       else  alert(errorMes);
      },
      error: function (res) {
       console.log(res)
       alert(res)
      }
     });
    }






    function suaphucap(e){
	  var id = $(e).attr("id") ;
	  $.ajax({
      url: '/qlluongthuong/layphucap',
      method:'get',
      data:{"id":id},
      dataType: 'json',
      contentType: "application/json",
      success: function (res) {
         let ten_pc = res.ten_pc
         let loai_pc = res.loai_pc
         let muc_pc = res.muc_pc
         $("input[name=saveNamePC]").val(ten_pc);
	     $("input[name=saveTypePC]").val(loai_pc);
	     $("input[name=saveLevelPC]").val(muc_pc);
	     $("#capnhatphucap").attr("idphucap",res.id)
	     $('#dialog2').modal('show');
      },
      error: function (res) {
       console.log(res)
      }
     });
	}


    function xoaphucap(e){
      var id = $(e).attr("id") ;

       if(confirm("Bạn chắc chắn muốn xóa")){
         $.ajax({
      url: '/qlluongthuong/xoaphucap',
      method:'get',
      data:{"id":id},
      dataType: 'json',
      contentType: "application/json",
      success: function (res) {
         if(res==200){ alert("Xóa thanh công") ; window.location.href="/qlluongthuong/qlphucap"}

         else alert("Xóa thất bại")
      },
      error: function (res) {
       console.log(res)
      }
     });
       }
    }
