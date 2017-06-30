cmake_minimum_required(VERSION 3.6 FATAL_ERROR)
project(libpqxx)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS)

option(BUILD_SHARED_LIBS "" ON)

add_library(pqxx
  src/binarystring.cxx
  src/connection_base.cxx
  src/connection.cxx
  src/cursor.cxx
  src/dbtransaction.cxx
  src/errorhandler.cxx
  src/except.cxx
  src/field.cxx
  src/largeobject.cxx
  src/nontransaction.cxx
  src/notification.cxx
  src/pipeline.cxx
  src/prepared_statement.cxx
  src/result.cxx
  src/robusttransaction.cxx
  src/row.cxx
  src/statement_parameters.cxx
  src/strconv.cxx
  src/subtransaction.cxx
  src/tablereader.cxx
  src/tablestream.cxx
  src/tablewriter.cxx
  src/transaction_base.cxx
  src/transaction.cxx
  src/util.cxx
  $<$<PLATFORM_ID:Windows>:win32/libpqxx.cxx>
)

target_include_directories(pqxx PUBLIC
  ${CMAKE_SOURCE_DIR}/include
  $<$<CXX_COMPILER_ID:MSVC>:${CMAKE_SOURCE_DIR}/config/sample-headers/compiler/VisualStudio2013>
)

target_link_libraries(pqxx PUBLIC CONAN_PKG::libpq)

target_compile_options(pqxx PUBLIC $<$<CXX_COMPILER_ID:MSVC>:/wd4100 /wd4267>)

target_compile_definitions(pqxx PUBLIC
  $<$<BOOL:${BUILD_SHARED_LIBS}>:PQXX_SHARED>
  $<$<PLATFORM_ID:Windows>:WIN32 _MBCS _WINDOWS>
)

set_target_properties(pqxx PROPERTIES PREFIX "lib" IMPORT_PREFIX "lib")
