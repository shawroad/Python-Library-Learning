function get_left_data() {
	$.ajax({
		url:"/left_data",
		success: function(data) {
		    option_left.xAxis.data = data.day
		    option_left.series[0].data = data.nums
			ec_left.setOption(option_left)
		},
		error: function(xhr, type, errorThrown) {
		}
	})
}

get_left_data()
setInterval(get_left_data, 1000*5)