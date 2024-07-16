import React from 'react';
import buyer from '../assets/images/buyer.jpg';

const BuyerSection = () => {
  return (
    <div className="bg-white rounded-lg shadow-lg overflow-hidden">
      <div className="p-4">
        <h2 className="text-xl font-semibold text-gray-800 mb-2">Find Your Perfect Home</h2>
        <p className="text-gray-600 mb-4">
          Compare property prices across neighborhoods to find the best deals within your budget.
        </p>
        <div className="border border-gray-200 rounded-lg overflow-hidden">

          {/* Replace with your actual comparison tool screenshot */}
          <img src={buyer} alt="Comparison Tool" className="w-full" />
        </div>
        <div className="mt-4">
          <button className="bg-blue-500 hover:bg-blue-600 text-white px-4 py-2 rounded-md shadow-md focus:outline-none">
            Compare Now
          </button>
        </div>
      </div>
    </div>
  );
};

export default BuyerSection;
