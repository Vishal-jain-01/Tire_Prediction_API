document.getElementById("submit-btn").addEventListener("click", async () => {
    const loadIndex = document.getElementById("loadIndex").value;
    const width = document.getElementById("width").value;
    const sellingPrice = document.getElementById("sellingPrice").value;
  
    const data = {
      LoadIndex: parseFloat(loadIndex),
      Width: parseFloat(width),
      SellingPrice: parseFloat(sellingPrice),
    };
  
    try {
      const response = await fetch("http://127.0.0.1:5000/predict", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
      });
  
      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }
  
      const result = await response.json();
      document.getElementById("output").innerText = `Tire Accuracy: ${result.tire_accuracy}`;
    } catch (error) {
      console.error("Error:", error);
      document.getElementById("output").innerText = "An error occurred.";
    }
  });
  
