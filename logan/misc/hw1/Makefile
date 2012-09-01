CPPFLAGS += -I$(GTEST_DIR)/include
CXXFLAGS += -g -Wall -Wextra

all : main.o utilities.o
	$(CXX) $(CPPFLAGS) $(CXXFLAGS) $^ -o hw1

main.o : main.cpp definitions.h
	$(CXX) $(CPPFLAGS) $(CXXFLAGS) -c main.cpp

utilities.o : utilities.cpp definitions.h
	$(CXX) $(CPPFLAGS) $(CXXFLAGS) -c utilities.cpp

clean :
	rm -f *.o hw1

