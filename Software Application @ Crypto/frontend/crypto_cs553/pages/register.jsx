import Head from "next/head";
import Footer from "./components/Footer";
import Header from "./components/Header";
import React from "react";
import {
  ChatIcon,
  ChipIcon,
  ChevronDoubleDownIcon,
  UserCircleIcon,
  UsersIcon,
  LightningBoltIcon,
  RefreshIcon,
} from "@heroicons/react/solid";
export default function chatPage() {
  const [message, setmessage] = React.useState("");
  const [name, setname] = React.useState("");
  const [pwd, setpwd] = React.useState("");
  const [status, setstatus] = React.useState("");
  // send messages
  let url = `/api/register_user/${name}/${pwd}`;
  const handleClick = () => {
    fetch(url)
      .then((res) => res.json())
      .then((data) => {
        setstatus(data["New member created"]);
      });
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
    <div className="flex flex-col items-center justify-center min-h-screen py-2 max-h-screen bg-gray-900">
      <Head>
        <title>Registration</title>
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <Header />
      <div className="flex justify-evenly text-gray-300">
        <div className="flex flex-col justify-start content-center m-3">
          <h1 className="text-3xl mb-3 text-center font-bold">
            Register New User
          </h1>
          {/* username input */}
          <input
            className="max-h-20 w-600 h-10 mt-3 text-xl font-bold rounded-md bg-gray-700 p-3"
            type="text"
            placeholder="Enter username.."
            onChange={(evt) => {
              setname(evt.target.value);
            }}
            style={textArea}
          />
          {/* password input */}
          <input
            className="max-h-20 w-600 h-10 mt-3 text-xl font-bold rounded-md bg-gray-700 p-3"
            type="text"
            placeholder="Enter password..."
            onChange={(evt) => {
              setpwd(evt.target.value);
            }}
            style={textArea}
          />

          {/* send button */}
          <div className="flex gap-1 justify-center mt-3">
            <LightningBoltIcon className="w-8 h-8 bg-green-500 rounded-lg mr-2" />
            <button
              className="w-8 h-8 text-2xl font-bold"
              onClick={handleClick}
            >
              Register
            </button>
          </div>

          <p
            className="max-h-80 h-40 w-600 text-gray-200 font-semibold"
            style={wrap}
          >
            {status}
          </p>
        </div>
      </div>
      <Footer />
    </div>
  );
}
