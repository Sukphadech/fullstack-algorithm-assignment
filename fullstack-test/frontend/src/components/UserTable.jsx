function UserTable({
  users,
  onEdit,
  onDelete,
}) {

  return (
    <div className="overflow-x-auto mt-6">

      <table className="w-full border border-gray-300 bg-white">

        <thead className="bg-gray-200">
          <tr>
            <th className="p-3 border">ID</th>
            <th className="p-3 border">Avatar</th>
            <th className="p-3 border">Name</th>
            <th className="p-3 border">Age</th>
            <th className="p-3 border">Email</th>
            <th className="p-3 border">Actions</th>
          </tr>
        </thead>

        <tbody>

          {users.map((user) => (

            <tr key={user.id}>

              <td className="p-3 border text-center">
                {user.id}
              </td>

              <td className="p-3 border text-center">
                <img
                  src={
                    user.avatar_url ||
                    "https://via.placeholder.com/50"
                  }
                  alt={user.name}
                  className="w-12 h-12 rounded-full mx-auto"
                />
              </td>

              <td className="p-3 border">
                {user.name}
              </td>

              <td className="p-3 border text-center">
                {user.age}
              </td>

              <td className="p-3 border">
                {user.email}
              </td>

              <td className="p-3 border text-center">

                <button
                  onClick={() => onEdit(user)}
                  className="
                    px-3
                    py-1
                    bg-yellow-500
                    text-white
                    rounded
                    mr-2
                  "
                >
                  Edit
                </button>

                <button
                  onClick={() => onDelete(user.id)}
                  className="
                    px-3
                    py-1
                    bg-red-600
                    text-white
                    rounded
                  "
                >
                  Delete
                </button>

              </td>

            </tr>

          ))}

        </tbody>

      </table>

    </div>
  );
}

export default UserTable;