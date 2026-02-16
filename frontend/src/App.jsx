import { useState } from "react";

function App() {
  const [formData, setFormData] = useState({
    MedInc: "",
    HouseAge: "",
    AveRooms: "",
    AveBedrms: "",
    Population: "",
    AveOccup: "",
    Latitude: "",
    Longitude: ""
  });

  const [prediction, setPrediction] = useState("");

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  const handlePredict = async () => {
    try {
      const response = await fetch("http://127.0.0.1:8000/predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          MedInc: Number(formData.MedInc),
          HouseAge: Number(formData.HouseAge),
          AveRooms: Number(formData.AveRooms),
          AveBedrms: Number(formData.AveBedrms),
          Population: Number(formData.Population),
          AveOccup: Number(formData.AveOccup),
          Latitude: Number(formData.Latitude),
          Longitude: Number(formData.Longitude)
        })
      });

      if (!response.ok) throw new Error("API Error");

      const data = await response.json();
      setPrediction(data.predicted_price);
    } catch (err) {
      console.error(err);
      alert("Failed to get prediction. Check backend server.");
    }
  };

  return (
    <div style={{ padding: "40px", maxWidth: "500px", margin: "auto" }}>
      <h1>House Price Predictor</h1>

      {Object.keys(formData).map((key) => (
        <div key={key} style={{ margin: "10px 0" }}>
          <label style={{ marginRight: "10px" }}>{key}:</label>
          <input
            type="number"
            step="0.01"
            name={key}
            placeholder={key}
            value={formData[key]}
            onChange={handleChange}
            style={{ padding: "5px", width: "200px" }}
          />
        </div>
      ))}

      <button
        onClick={handlePredict}
        style={{
          marginTop: "20px",
          padding: "10px 20px",
          fontSize: "16px",
          cursor: "pointer"
        }}
      >
        Predict
      </button>

      {prediction && (
        <h2 style={{ marginTop: "20px" }}>
          Predicted Price: ₹{Number(prediction).toLocaleString("en-IN")}
        </h2>
      )}
    </div>
  );
}

export default App;

