document.addEventListener('DOMContentLoaded', function() {
  var ctx = document.getElementById('cancerChart');
  if (!ctx) return;
  new Chart(ctx, {
    type: 'bar',
    data: {
      labels: ['갑상선암', '폐암', '위암', '대장암', '유방암', '전립선암', '간암'],
      datasets: [{
        data: [30676, 29960, 29493, 29030, 24933, 16803, 15605],
        backgroundColor: ['#B4B2A9','#B4B2A9','#D85A30','#B4B2A9','#B4B2A9','#B4B2A9','#B4B2A9'],
        borderRadius: 6,
        barPercentage: 0.7
      }]
    },
    options: {
      responsive: true,
      plugins: { legend: { display: false }, tooltip: { enabled: true } },
      scales: {
        y: { display: false },
        x: { grid: { display: false }, ticks: { font: { size: 12, weight: '600' }, color: '#64748B' } }
      },
      animation: { duration: 1200 }
    },
    plugins: [{
      afterDatasetsDraw: function(chart) {
        var ctx2 = chart.ctx;
        chart.data.datasets[0].data.forEach(function(val, i) {
          var meta = chart.getDatasetMeta(0).data[i];
          ctx2.fillStyle = '#334155';
          ctx2.font = 'bold 12px sans-serif';
          ctx2.textAlign = 'center';
          ctx2.fillText(val.toLocaleString(), meta.x, meta.y - 8);
        });
      }
    }]
  });
});
