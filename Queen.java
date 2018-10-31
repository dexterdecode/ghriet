
public class Queen {
	public static int[] e = new int[20];

	public static int count;

	public static void main(String[] args) {
		int n = 8, i, j;
		System.out.print("Press any Key to Solve 8 Queen's Problem");
		queen(1, n);
	}

	public static void print(int n) {
		System.out.println("\n\nSolution:" + ++count + "\n");
		for(int i = 1; i <= n; ++i) {
			System.out.print("\t" + i);
		}
		for(int i = 1; i <= n; ++i) {
			System.out.print("\n\n" + i);
			for(int j = 1; j <= n; ++j) {
				if(e[i] == j) {
					System.out.print("\tQ");
				} else {
					System.out.print("\t-");
				}
			}
		}
	}

	public static boolean place(int row, int column) {
		for(int i = 1; i <= row - 1; ++i) {
			if(e[i] == column) {
				return false;
			} else if(Math.abs(e[i] - column) == Math.abs(i - row)) {
				return false;
			}
		}
		return true;
	}

	public static void queen(int row, int n) {
		for(int column = 1; column <= n; ++column) {
			if(place(row, column)) {
				e[row] = column;
				if(row == n) {
					print(n);
				} else {
					queen(row + 1, n);
				}
			}
		}
	}
}