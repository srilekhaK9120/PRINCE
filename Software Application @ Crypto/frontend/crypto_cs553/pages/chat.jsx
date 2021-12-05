import Head from "next/head";
import Link from "next/link";
import Footer from "./components/Footer";
import Header from "./components/Header";

export default function chat() {
  const startServer=()=>{
    fetch('/api/start_server/')
  }
  const stopServer=()=>{
    fetch('/api/stop')
  }
  return (
    <div className="flex flex-col items-center justify-center min-h-screen py-2 bg-gray-900">
      <Head>
        <title>Cryptography_CS553</title>
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <Header />

      <main className="flex flex-col items-center justify-center w-full flex-1 px-20 text-center text-gray-300">
        <h1 className="text-5xl font-bold">GroupChat Application</h1>
        <p className="mt-3 text-2xl font-bold">
          "Secure group chat application backed by prince cipher"
          {/* <code className="p-1 ml-1 font-mono text-lg bg-gray-600 rounded-md">
            <a href="/">github link</a>
          </code> */}
        </p>

        <div className="flex flex-wrap items-center justify-around max-w-4xl mt-6 sm:w-full">
          <button
            className="p-6 mt-6 text-left border w-96 rounded-xl hover:text-green-600 focus:text-green-600 hover:font-bold"
            onClick={startServer}
          >
            <h3 className="text-2xl font-bold">Start Server &rarr;</h3>
            <p className="mt-4 text-xl">
              Start the messaging server in the backend.
            </p>
          </button>

          <a
            href="/chatPage"
            className="p-6 mt-6 text-left border w-96 rounded-xl hover:text-green-600 focus:text-green-600 hover:font-bold"
          >
            <h3 className="text-2xl font-bold">Start Chat &rarr;</h3>
            <p className="mt-4 text-xl">
              Enter name and password, then send and view messages.
            </p>
          </a>

          <button
            className="p-6 mt-6 text-left border w-96 rounded-xl hover:text-green-600 focus:text-green-600 hover:font-bold"
            onClick={stopServer}
          >
            <h3 className="text-2xl font-bold">Stop Server &rarr;</h3>
            <p className="mt-4 text-xl">
              Stops the messaging server in the backend.
            </p>
          </button>

          <a
            href="/register"
            className="p-6 mt-6 text-left border w-96 rounded-xl hover:text-green-600 focus:text-green-600 hover:font-bold"
          >
            <h3 className="text-2xl font-bold">Register New User &rarr;</h3>
            <p className="mt-4 text-xl">
              Register a new user into group chat messaging.
            </p>
          </a>

          <p
            className="p-6 mt-6 text-left border w-192 rounded-xl  focus:text-green-600"
          >
            <h3 className="text-2xl font-bold hover:text-green-600">
              default group members &rarr;
            </h3>
            <p className="mt-4 text-xl">
              <code className="p-2 m-2 font-semibold font-mono text-lg bg-gray-600 rounded-md hover:text-blue-400">
                kishore(abc123)
              </code>
              <code className="p-2 m-2 font-semibold font-mono text-lg bg-gray-600 rounded-md hover:text-blue-400">
                vivek(123)
              </code>
              <code className="p-2 m-2 font-semibold font-mono text-lg bg-gray-600 rounded-md hover:text-blue-400">
                srilekha(abc)
              </code>
              <code className="p-2 m-2 font-semibold font-mono text-lg bg-gray-600 rounded-md hover:text-blue-400">
                guest1(guest1)
              </code>
              <code className="p-2 m-2 font-semibold font-mono text-lg bg-gray-600 rounded-md hover:text-blue-400">
                guest2(guest2)  
              </code>
            </p>
          </p>
        </div>
      </main>
      <Footer />
    </div>
  );
}
