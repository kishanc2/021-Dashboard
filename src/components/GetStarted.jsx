import styles from "../style";
import { arrowUp } from "../assets";

const GetStarted = () => (
  <div className={`${styles.flexCenter} w-[140px] h-[140px] rounded-full bg-blue-gradient p-[2px] cursor-pointer`}>
    <div className={`${styles.flexCenter} flex-col bg-primary w-[100%] h-[100%] rounded-full`}>
      <div className={`${styles.flexStart} flex-row`}>
        <p className="font-poppins font-medium text-[18px] leading-[23.4px]">
          {/* Get */}

          <a href = "src/startbootstrap-sb-admin-2-gh-pages/index.html">
      <button>
      <span className="text-gradient">
        Get Started
        </span>
      </button>
    </a>
        </p>
        <img href= "src/startbootstrap-sb-admin-2-gh-pages/index.html" src={arrowUp} alt="arrow-up" className="w-[23px] h-[23px] object-contain" />
      </div>
    </div>

    
    
  </div>
);

export default GetStarted;
