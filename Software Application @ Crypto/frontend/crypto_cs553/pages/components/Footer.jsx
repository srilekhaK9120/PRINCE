import {FireIcon} from '@heroicons/react/solid'
function Footer() {
    return (
        <footer className="fixed bottom-0 flex items-center justify-center w-full h-50 border-tb text-white ">
        <a
          className="flex items-center justify-center hover:text-blue-400 text-lg"
          href="/"
          target="_blank"
          rel="noopener noreferrer"
        >

          <p>&copy; Team <FireIcon className="inline w-5 h-5 animate-pulse"/> <span className="font-bold animate-pulse">ILLUMINATI </span> <span className="font-extrabold">|</span> CS553_Cryptography <span className="font-extrabold">|</span> IITBhilai</p>
        </a>
      </footer>
    )
}

export default Footer
