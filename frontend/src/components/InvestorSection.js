import React from 'react';
import investors from '../assets/images/investors.jpg';

const InvestorSection = () => {
  return (
    <div className="bg-white rounded-lg shadow-lg overflow-hidden">
      <div className="p-4">
        <h2 className="text-xl font-semibold text-gray-800 mb-2">Maximize Your Investments</h2>
        <p className="text-gray-600 mb-4">
          Access historical price trends and future predictions to make smart investment choices.
        </p>
        <div className="border border-gray-200 rounded-lg overflow-hidden">

          {/* Replace with your actual interactive chart or mockup */}
          <img src={investors} alt="Investors Chart" className="w-full" />
        </div>
        <div className="mt-4">
          <button className="bg-blue-500 hover:bg-blue-600 text-white px-4 py-2 rounded-md shadow-md focus:outline-none">
            View Investment Trends
          </button>
        </div>
      </div>
    </div>
  );
};

export default InvestorSection;
