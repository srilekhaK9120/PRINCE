import {
  ChatIcon,
  ChipIcon,
  ChevronDoubleDownIcon,
  UserCircleIcon,
  UsersIcon,
  LightningBoltIcon,
} from "@heroicons/react/solid";
import React from "react";
function Sendbox(props) {
  const m1 = props.m1;
  const m2 = props.m2;
  const placeholderMessage = props.m3;
  const type = props.m4;
  const m5 = props.m5;
  console.log(m5)
  const [message, setmessage] = React.useState("");
  const [returnMessage, setreturnMessage] = React.useState("");
  const [key, setkey] = React.useState("");
  let url = `/api/${type}/${message}/${key}`;
  const handleClick = () => {
    fetch(url)
      .then((res) => res.json())
      .then((data) => setreturnMessage(data[m5]));
  };
  const textArea = {
    border: "none",
    overflow: "auto",
    outline: "none",
    boxShadow: "none",
    resize: "none",
  };
  const wrap = {
    overflow: "auto",
    overflowWrap: "break-word",
  };
  return (
    <div className="flex flex-col justify-center content-center m-3">
      <h1 className="text-3xl mb-4 text-center font-bold">{m1}</h1>
      <textarea
        className="w-600 h-40 max-h-80 text-xl font-bold rounded-md bg-gray-700 p-3 focus:outline-0"
        type="text"
        placeholder={placeholderMessage}
        onChange={(evt) => {
          setmessage(evt.target.value);
        }}
        style={textArea}
      />
      <input
        className="max-h-20 w-600 h-10 mt-3 text-xl font-bold rounded-md bg-gray-700 p-3"
        type="text"
        placeholder="Enter the key here.."
        onChange={(evt) => {
          setkey(evt.target.value);
        }}
        style={textArea}
      />
      <div className="flex gap-1 justify-center mt-3">
        <LightningBoltIcon className="w-8 h-8 bg-green-500 rounded-lg mr-2" />
        <button className="w-8 h-8 text-2xl font-bold" onClick={handleClick}>
          {m2}
        </button>
      </div>
      <div className="flex justify-center">
        <ChevronDoubleDownIcon className="w-32 h-w-32 mt-3 animate-pulse text-green-700" />
      </div>
      <p
        className="max-h-80 h-40 w-600 text-gray-200 font-semibold"
        style={wrap}
      >
        {returnMessage}
      </p>
    </div>
  );
}

export default Sendbox;
