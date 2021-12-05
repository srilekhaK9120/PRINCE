import Image from "next/image";
function Header() {
  return (
    <div className="fixed top-0">
      <div className="flex flex-col justify-between items-center">
        <div className="relative w-24 h-24 mt-10">
          <a
            href="https://www.iitbhilai.ac.in/"
            target="_blank"
            rel="noopener noreferrer"
          >
            <Image src="/Logo.png" layout="fill" objectFit="contain" />
          </a>
        </div>
        <div className="mt-1 text-xl text-white font-bold border-b-2">
          <p>CS553</p>
        </div>
      </div>
    </div>
  );
}

export default Header;
