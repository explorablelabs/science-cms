// JS Goes here - ES6 supported
import SmilesDrawer from 'smiles-drawer';
import Chart from 'chart.js';
import 'chartjs-chart-box-and-violin-plot';

// Draw all the molecules
SmilesDrawer.apply();

if (window.netlifyIdentity) {
  window.netlifyIdentity.on("init", user => {
    if (!user) {
      window.netlifyIdentity.on("login", () => {
        document.location.href = "/admin/";
      });
    }
  });
}
