import { useState } from "react";
import { ReactMediaRecorder } from "react-media-recorder";
import axios from "axios";
import RecordMessage from "./RecordMessage";

const Controller = () => {
  const [isLoading, setIsLoading] = useState(false);
  const [messages, setMessages] = useState(false);

  return (
    <div className="flex items-center justify-center text-center h-screen">
      <RecordMessage />
    </div>
  );
};

export default Controller;
