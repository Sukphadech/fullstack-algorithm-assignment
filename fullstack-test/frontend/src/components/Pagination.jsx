function Pagination({
  start,
  limit,
  total,
  setStart,
}) {

  const hasPrev = start > 0;

  const hasNext = start + limit < total;


  return (
    <div className="flex justify-center gap-4 mt-6">

      <button
        onClick={() => setStart(start - limit)}
        disabled={!hasPrev}
        className="
          px-4
          py-2
          bg-gray-800
          text-white
          rounded
          disabled:opacity-50
        "
      >
        Previous
      </button>

      <button
        onClick={() => setStart(start + limit)}
        disabled={!hasNext}
        className="
          px-4
          py-2
          bg-gray-800
          text-white
          rounded
          disabled:opacity-50
        "
      >
        Next
      </button>

    </div>
  );
}

export default Pagination;