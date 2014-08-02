var data_reuniao = $('#data_visita').datepicker({
                    onRender: function(date) {
                        return date
                    },
                    format: 'dd/mm/yyyy'
                }).on('changeDate', function(ev) {
                    data_reuniao.hide();
                }).data('datepicker');

$('#humor').selectize({
					create: true,
					sortField: {
						field: 'id',

					},
					dropdownParent: 'body'
				});