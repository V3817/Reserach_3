import { useState } from "react";
import axios from "axios";

import ReactMarkdown from "react-markdown";

import { FiDownload, FiCopy } from "react-icons/fi";

import jsPDF from "jspdf";
import html2canvas from "html2canvas";

const API_URL = import.meta.env.VITE_API_URL;



function App() {

  const [topic, setTopic] = useState("");

  const [report, setReport] = useState("");

  const [feedback, setFeedback] = useState("");

  const [loading, setLoading] = useState(false);

  const [sources, setSources] = useState([]);

  const [status, setStatus] = useState("");



  // =====================================================
  // RUN RESEARCH
  // =====================================================

  const handleResearch = async () => {

    if (!topic.trim()) return;

    setLoading(true);

    setReport("");

    setFeedback("");

    setSources([]);

    try {

      setStatus("Searching Sources...");

      const response = await axios.post(
        `${API_URL}/research`,
        {
          topic: topic
        }
      );

      setStatus("Generating Report...");

      setReport(response.data.report);

      setFeedback(response.data.feedback);

      setSources(response.data.sources || []);

      setStatus("Research Completed");

    } catch (error) {

      console.error(error);

      setStatus("Something went wrong");

    }

    setLoading(false);
  };



  // =====================================================
  // COPY REPORT
  // =====================================================

  const copyReport = async () => {

    await navigator.clipboard.writeText(report);

    alert("Report copied!");
  };



  // =====================================================
  // DOWNLOAD MARKDOWN
  // =====================================================

  const downloadMarkdown = () => {

    const blob = new Blob(
      [report],
      { type: "text/markdown" }
    );

    const url = window.URL.createObjectURL(blob);

    const a = document.createElement("a");

    a.href = url;

    a.download = "research_report.md";

    a.click();

    window.URL.revokeObjectURL(url);
  };



  // =====================================================
  // DOWNLOAD PDF
  // =====================================================

  const downloadPDF = async () => {

    const input = document.getElementById(
      "report-section"
    );

    const canvas = await html2canvas(input);

    const imgData = canvas.toDataURL("image/png");

    const pdf = new jsPDF(
      "p",
      "mm",
      "a4"
    );

    const pdfWidth =
      pdf.internal.pageSize.getWidth();

    const pdfHeight =
      (canvas.height * pdfWidth) / canvas.width;

    pdf.addImage(
      imgData,
      "PNG",
      0,
      0,
      pdfWidth,
      pdfHeight
    );

    pdf.save("research_report.pdf");
  };



  // =====================================================
  // UI
  // =====================================================

  return (

    <div
      style={{
        minHeight: "100vh",
        background: "#0f172a",
        color: "white",
        padding: "40px",
        fontFamily: "sans-serif"
      }}
    >

      {/* ============================================= */}
      {/* HEADER */}
      {/* ============================================= */}

      <div
        style={{
          marginBottom: "40px"
        }}
      >

        <h1
          style={{
            fontSize: "42px",
            marginBottom: "10px"
          }}
        >
          Deep Research AI
        </h1>

        <p
          style={{
            color: "#94a3b8"
          }}
        >
          Autonomous Multi-Agent Research System
        </p>

      </div>



      {/* ============================================= */}
      {/* INPUT */}
      {/* ============================================= */}

      <div
        style={{
          display: "flex",
          gap: "10px",
          marginBottom: "30px"
        }}
      >

        <input
          type="text"
          placeholder="Enter research topic..."
          value={topic}
          onChange={(e) => setTopic(e.target.value)}
          style={{
            flex: 1,
            padding: "16px",
            borderRadius: "12px",
            border: "none",
            background: "#1e293b",
            color: "white",
            fontSize: "16px"
          }}
        />

        <button
          onClick={handleResearch}
          disabled={loading}
          style={{
            padding: "16px 24px",
            borderRadius: "12px",
            border: "none",
            background: "#38bdf8",
            color: "black",
            fontWeight: "bold",
            cursor: "pointer"
          }}
        >
          {loading ? "Researching..." : "Start Research"}
        </button>

      </div>



      {/* ============================================= */}
      {/* STATUS */}
      {/* ============================================= */}

      {status && (

        <div
          style={{
            background: "#1e293b",
            padding: "20px",
            borderRadius: "16px",
            marginBottom: "30px"
          }}
        >

          <h3>Status</h3>

          <p>{status}</p>

        </div>
      )}



      {/* ============================================= */}
      {/* REPORT */}
      {/* ============================================= */}

      {report && (

        <div
          style={{
            background: "#1e293b",
            padding: "30px",
            borderRadius: "20px",
            marginBottom: "30px"
          }}
        >

          <div
            style={{
              display: "flex",
              justifyContent: "space-between",
              alignItems: "center",
              marginBottom: "20px"
            }}
          >

            <h2>Research Report</h2>

            <div
              style={{
                display: "flex",
                gap: "10px"
              }}
            >

              <button
                onClick={copyReport}
                style={buttonStyle}
              >
                <FiCopy />
              </button>

              <button
                onClick={downloadMarkdown}
                style={buttonStyle}
              >
                .md
              </button>

              <button
                onClick={downloadPDF}
                style={buttonStyle}
              >
                <FiDownload />
              </button>

            </div>

          </div>



          <div id="report-section">

            <ReactMarkdown>
              {report}
            </ReactMarkdown>

          </div>

        </div>
      )}



      {/* ============================================= */}
      {/* FEEDBACK */}
      {/* ============================================= */}

      {feedback && (

        <div
          style={{
            background: "#1e293b",
            padding: "30px",
            borderRadius: "20px",
            marginBottom: "30px"
          }}
        >

          <h2>Critic Feedback</h2>

          <ReactMarkdown>
            {feedback}
          </ReactMarkdown>

        </div>
      )}



      {/* ============================================= */}
      {/* SOURCES */}
      {/* ============================================= */}

      {sources.length > 0 && (

        <div>

          <h2
            style={{
              marginBottom: "20px"
            }}
          >
            Sources
          </h2>

          <div
            style={{
              display: "grid",
              gridTemplateColumns:
                "repeat(auto-fit, minmax(300px, 1fr))",
              gap: "20px"
            }}
          >

            {sources.map((source, index) => (

              <div
                key={index}
                style={{
                  background: "#1e293b",
                  padding: "20px",
                  borderRadius: "16px"
                }}
              >

                <h3
                  style={{
                    marginBottom: "10px"
                  }}
                >
                  {source.title}
                </h3>

                <p
                  style={{
                    color: "#cbd5e1",
                    marginBottom: "10px"
                  }}
                >
                  {source.snippet}
                </p>

                <a
                  href={source.url}
                  target="_blank"
                  rel="noreferrer"
                  style={{
                    color: "#38bdf8"
                  }}
                >
                  Visit Source
                </a>

              </div>

            ))}

          </div>

        </div>
      )}

    </div>
  );
}



// =========================================================
// BUTTON STYLE
// =========================================================

const buttonStyle = {
  padding: "10px 14px",
  borderRadius: "10px",
  border: "none",
  background: "#334155",
  color: "white",
  cursor: "pointer",
  display: "flex",
  alignItems: "center",
  justifyContent: "center"
};



export default App;