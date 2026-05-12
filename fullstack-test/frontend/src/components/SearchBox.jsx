function SearchBox({ search, setSearch }) {

  return (
    <input
      type="text"
      placeholder="Search by name or email..."
      value={search}
      onChange={(e) => setSearch(e.target.value)}
      className="
        w-full
        md:w-80
        p-3
        border
        rounded-lg
        bg-white
      "
    />
  );
}

export default SearchBox;