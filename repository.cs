using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.EntityFrameworkCore;
using contextapp.Models;

namespace UsuarioRepository.Repositories
{
    public class UsuarioRepository : IUsuarioRepository
    {
        private readonly AppDbContext _context;

        public UsuarioRepository(AppDbContext context)
        {
            _context = context;
        }

        public list<UsuarioRepository> TraerUsuariosAsync()
        {
            return  _context.Usuarios.ToList(); // Operación asíncrona
        }
    }
}
